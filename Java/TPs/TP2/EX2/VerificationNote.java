package Java.TPs.TP2.EX2;

public class VerificationNote {
    public static void main(String[] args) {
        String note = "C";
        switch (note) {
            case "A":
                System.out.println("Très bien");
                break;
            case "B":
                System.out.println("Bien");
                break;
            case "C":
                System.out.println("Insuffisant");
                break;
            default:
                System.out.println("Note non valide");
                break;
        }
    }
}
