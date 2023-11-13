package Java.TPs.TP5;

public class Main {
    public static void main(String[] args) {
        Cercle c1 = new Cercle("cercle", 12);
        Rectangle r1 = new Rectangle("rectangle", 10, 12.5);

        c1.quisuije();
        r1.quisuije();

        System.out.println(c1.aire());

    }
}
