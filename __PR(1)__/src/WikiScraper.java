

import java.io.*;
import java.util.*;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class WikiScraper {

    public static HashSet<String> primes_List = new HashSet<String>();

    public void getWarframes() {
        try {

            // Seite laden und parsen
            Document doc = Jsoup.connect("https://warframe.fandom.com/wiki/Warframes")
                .userAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
                .referrer("https://www.google.com")
                .timeout(10 * 1000)
                .get();

            // Alle Warframe-Divs finden
            Elements warframes = doc.select("div.WarframeNavBox");

            for (Element frame : warframes) {
                Element primeName = frame.selectFirst("span[style=\"color:gold;\"]");

                if (primeName != null && !primeName.text().equalsIgnoreCase("excalibur")) {
                    String prime = primeName.text().toLowerCase() + " prime";
                    primes_List.add(prime);
}
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    
}

