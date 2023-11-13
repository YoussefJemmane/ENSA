package Java.TPs.TP4;

public class Animal {
    public int nbPattes;
    public String nom;

    public Animal(int nbPattes, String nom) {
        this.nbPattes = nbPattes;
        this.nom = nom;
    }

    public String toString(int nbPattes, String nom) {
        return "L'animal " + nom + " contient " + nbPattes + " pattes";
    }

    public void afficher() {
        System.out.println(toString(nbPattes, nom));
    }

}
