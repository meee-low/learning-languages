#!/bin/bash

build_folder="./build"

# Function to compile and run a Scala file
compile_and_run() {
  # Check if the Scala file exists
  if [ ! -f "$1" ]; then
    echo "Error: Scala file '$1' not found."
    exit 1
  fi

  mkdir $build_folder -p
  compilation_flags="-Werror -deprecation -d $build_folder -classpath $build_folder -explain -unchecked"

  # Compile the Scala file
  echo javac "$compilation_flags $1"
  echo "Compiling..."
  javac $compilation_flags $1
  echo "Finished compiling..."
  echo "=================="

  # Check if compilation was successful
  if [ $? -eq 0 ]; then
    # Extract the base name of the file (without extension)
    filename=$(basename -- "$1")
    filename_noext="${filename%.*}"

    # Run the compiled class file
    cd $build_folder
    java $filename_noext
    cd ..

    # Check if the clean after flag is set
    if [ "$clean_after" = true ]; then
      # Remove the class file and any tasty files
      cd $build_folder
      rm -f "$filename_noext.class" $filename_noext.tasty $filename_noext\$$package*
      cd ..
    fi
  else
    echo "Compilation failed for '$1'."
    exit 1
  fi
}

# Function to clean .class and .tasty files in the current folder and subfolders
clean_files() {
  rm -f *.class *.tasty
  rm -f $build_folder/*
  # find . -type f -name "*.class" -o -name "*.tasty" -exec rm -f {} \;
}

# Parse command-line arguments
while [ $# -gt 0 ]; do
  case "$1" in
    -ca|--clean-after|-run)
      clean_after=true
      shift
      ;;
    --clear)
      clean_files
      exit 0
      ;;
    *)
      compile_and_run "$1"
      exit 0
      ;;
  esac
done

# If no arguments provided, display usage
echo "Usage: $0 [-ca | --clear] <Scala file>"
exit 1
