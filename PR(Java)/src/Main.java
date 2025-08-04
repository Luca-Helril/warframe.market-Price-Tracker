import javafx.application.Application;

public class Main {
   public static void main(String[] args) {
        


        gui_aufruf();
        

        //wiki_aufruf();


        

    }

    public static void gui_aufruf() {
        Application.launch(Ui.class);
    }

    public static void wiki_aufruf() {

            WikiScraper scraper = new WikiScraper();
            scraper.getWarframes();
        
            System.out.println("Gefundene Prime-Warframes:");
            int i = 0;
            for (String prime : WikiScraper.primes_List) {
            //System.out.println("- " + prime);
            // (key=name, value=list=serch(name))
                i++;
            }System.out.println(i);
        }
}
