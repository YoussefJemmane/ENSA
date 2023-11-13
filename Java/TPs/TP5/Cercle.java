package Java.TPs.TP5;

public class Cercle extends Figure {
    double R;

    Cercle(String nom, double R) {
        super(nom);
        this.R = R;
    }

    @Override
    public double aire() {
        return Math.PI * R * R;
    }
}
