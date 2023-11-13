package Java.TPs.TP5;

abstract public class Figure {
    private String nom;

    private Figure(String nom) {
        this.nom = nom;
    }

    abstract public double aire();

    public void quisuije() {
        System.out.println(nom);
    }


    
}
