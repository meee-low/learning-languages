public class ComplexNumbers {
    public static void main(String[] args) {
        ComplexNumbers complexNumbers = new ComplexNumbers();
        Complex a = complexNumbers.new Complex(1, 2);
        Complex b = complexNumbers.new Complex(-1f, 0f);

        System.out.println(a);
        System.out.println(b);
        System.out.println(a.add(b));
        System.out.println(a.mult(b));


        Quaternion i = complexNumbers.new Quaternion(0,1,0,0);
        Quaternion j = complexNumbers.new Quaternion(0,0,1,0);

        System.out.println(i.mult(j));
        System.out.println(j.mult(i));
    }

    class Complex {
        float re;
        float im;
        public Complex(float re, float im) {
            this.re = re;
            this.im = im;
        }

        public Complex add(Complex z) {
            return new Complex(re + z.re, im + z.im);
        }

        public Complex mult(Complex z) {
            // (a + bi)(c + di) =
            // ac + adi + bci - bd
            return new Complex(re*z.re - im*z.im, re*z.im + im*z.re);
        }

        public String toString() {
            return String.format("%s + %sj", re, im);
        }
    }

    class Quaternion {
        float re;
        float i;
        float j;
        float k;

        public Quaternion(float re, float i, float j, float k) {
            this.re = re;
            this.i = i;
            this.j = j;
            this.k = k;
        }

        public Quaternion mult(Quaternion q) {
            // (a + bi + cj + dk)*(u + vi + wj + xk) =
            // a(u+vi+wj+xk) + bi(u+vi+wj+xk) + cj(u+vi+wj+xk) + dk(u+vi+wj+xk) =
            // (au + avi + awj + axk) + (bui -bv +bwk -bxj) + ...
            float newRe = re * q.re - i * q.i - j * q.j - k * q.k;
            float newI = re * q.i + i * q.re + j * q.k - k * q.j;
            float newJ = re * q.j - i * q.k + j * q.re + k * q.i;
            float newK = re * q.k + i * q.j - j * q.i + k * q.re;

            return new Quaternion(newRe, newI, newJ, newK);
        }

        public String toString() {
            return String.format("%s + %si + %sj + %sk", re, i, j, k);
        }
    }
}

