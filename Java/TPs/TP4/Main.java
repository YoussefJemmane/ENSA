package Java.TPs.TP4;

public class Main {
    public static void main(String[] args) {
        Lapin l1 = new Lapin(4, "Lapin");
        Autruche a1 = new Autruche(2, "autr");
        a1.afficher();
        System.out.println(l1.toString(l1.nbPattes, l1.nom));
        System.out.println(a1.toString(a1.nbPattes, a1.nom));
    }
}
