class Personne {
    String nom;
    String prenom;
    int age;

    public void modifierage(int Age) {
        this.age = Age;
    }

    public static void main(String[] args) {
        Personne p1 = new Personne();
        p1.nom = "Jemmane";
        p1.prenom = "Youssef";
        p1.age = 20;
        Personne p2 = new Personne();
        p2.nom = "El Alaoui";
        p2.prenom = "Ayoub";
        p2.age = 20;
        p1.modifierage(21);
        p2.modifierage(22);
        System.out.println("Nom: " + p1.nom + " Prenom: " + p1.prenom + " Age: " + p1.age);
        System.out.println("Nom: " + p2.nom + " Prenom: " + p2.prenom + " Age: " + p2.age);

    }
}
