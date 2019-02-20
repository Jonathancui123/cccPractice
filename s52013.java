import java.util.Scanner;
public class ccc13s5 {
	public static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		int n = sc.nextInt();
		int cost = 0;
		while (n > 1) {
			double o = (int) (Math.sqrt(n)) + 1;
			int p = 2;
			while (p <= o && n % p != 0) {
				p += 1;
			}
			if (p < n && n % p == 0) {
				int q = n / p;
				n -= q;
				cost += n / q;
			} else {
				n -= 1;
				cost += n;
			}
		}
		System.out.println(cost);
	}
}
