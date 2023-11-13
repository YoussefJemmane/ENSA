package Java.TPs.TP4;

public class Autruche extends Animal {
    public Autruche(int nbPattes, String nom) {
        super(nbPattes, nom);
    }

    public String toString(int nbPattes, String nom) {
        return "L'autruche " + nom + " contient " + nbPattes + " pattes";
    }
}
