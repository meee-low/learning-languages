# Compiler and compiler flags
CXX := clang++
CXXFLAGS := -std=c++11 -Wall -Wextra -pedantic

# Directory where source files are located
SRC_DIR := .

# Directory where binary/executable files will be generated
BIN_DIR := ./bin

# List all source files (assuming they have a .cpp extension)
SRCS := $(wildcard $(SRC_DIR)/*.cpp)

# Generate a list of corresponding object files
OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(BIN_DIR)/%.o,$(SRCS))

# Name of the final executable
EXEC := learning-languages

# Default target: build everything
all: $(BIN_DIR)/$(EXEC)

# Target to check if everything still compiles
.PHONY: check
check:
	$(CXX) $(CXXFLAGS) -fsyntax-only $(SRCS)
	@echo "All files are syntatically valid."

# Rule to link the object files and create the executable
$(BIN_DIR)/$(EXEC): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Rule to compile individual source files into object files
$(BIN_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -c -o $@ $<
	$(CXX) $(CXXFLAGS) -o $(BIN_DIR)/$* $@

# Create the binary directory if it doesn't exist
$(BIN_DIR):
	mkdir -p $(BIN_DIR)


# Target to delete all compiled files
clean:
	rm -rf $(BIN_DIR)
	mkdir $(BIN_DIR)

.PHONY: all check clean
