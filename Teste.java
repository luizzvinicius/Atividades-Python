import java.io.Console;
import java.util.regex.Pattern;

public class Teste {
    public static void main(String[] args) {
        try {
            var scan = System.console();
            var palavra = lerString(scan, "Digite seu nome: ", "Nome inválido");
            System.out.println(palavra);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static String lerString(Console scan, String msg, String erroMessage) {
        String palavra;
        while (true) {
            System.out.print(msg);
            palavra = scan.readLine().strip().toLowerCase();
            if (!Pattern.matches("^[a-zÀ-ÿ\s]+$", palavra)) {
                System.out.println(erroMessage + "\n");
                continue;
            }
            return palavra;
        }
    }
}