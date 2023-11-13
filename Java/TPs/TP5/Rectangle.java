package Java.TPs.TP5;

public class Rectangle extends Figure {
    double L;
    double l;

    Rectangle(String nom, double L, double l) {
        super(nom);
        this.l = l;
        this.L = L;
    }

    @Override
    public double aire() {
        return L * l;
    }

}
