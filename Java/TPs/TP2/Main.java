public class Main{
    public static void main(String[] args){
        Personne p1 = new Personne();
        p1.setnom("Jemmane");
        p1.setprenom("Youssef");
        p1.setage(20);
        
        System.out.print("Nom : "+p1.getnom()+", Prenom : "+p1.getprenom()+", Age : "+p1.getage());
    }
}