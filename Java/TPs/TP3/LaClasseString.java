package Java.TPs.TP3;

public class LaClasseString {
    String nom = "Jemmane";
    String prenom = "Youssef";
    public Boolean estEgal() {
        return this.nom.equals(this.prenom);
    }
    public int longueurdenom() {
        return this.nom.length();
    }
    public int longueurdeprenom() {
        return this.prenom.length();
    }
    public char deuxiemecaracteredenom() {
        return this.nom.charAt(1);
    }
    public char deuxiemecaracteredeprenom() {
        return this.prenom.charAt(1);
    }
    public String addmr() {
        return "Mr " + this.nom;
    }

    public static void main(String[] args) {
        LaClasseString laClasseString = new LaClasseString();
        System.out.println("Votre nom est " + laClasseString.addmr()  + " " +laClasseString.prenom + " Votre nom est egal a votre prenom ? " + laClasseString.estEgal() + " La longueur de votre nom est " + laClasseString.longueurdenom() + " La longueur de votre prenom est " + laClasseString.longueurdeprenom() + " Le deuxieme caractere de votre nom est " + laClasseString.deuxiemecaracteredenom() + " Le deuxieme caractere de votre prenom est " + laClasseString.deuxiemecaracteredeprenom());
    }
}
