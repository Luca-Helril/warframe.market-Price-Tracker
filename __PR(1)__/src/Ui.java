import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.control.Tooltip;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class Ui extends Application{
    
    private TextField tfNumber;
    private Button btnCalc;
    private EventHandler<ActionEvent> handler;
    private Label lblStatus;
    private Label lblResult;
    
    @Override
    public void start(Stage primaryStage) {
        // GUI-Komponenten
        Label lbl = new Label("Name");
        tfNumber = new TextField();
        btnCalc = new Button("Cal_culate");
        btnCalc.setMnemonicParsing(true);

        lblResult = new Label("Warframes: ");
        
        
        
        

        // EventHandler zur Buttonaktion
        // wenn der Button gedrückt wird, werden die teiler von der zahl in Textfelt ausgerechnet und in Label ausgegeben
        handler = new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                
                // was gemacht werden soll
            }
        };
        lblStatus = new Label("");
        
        btnCalc.setOnAction(handler);
        
        tfNumber.textProperty().addListener( (oberserved, oldvalue, newvalue) -> checkInput() );
        checkInput(); // methode wird am anfag ausgeführt
        
        // ScrollPane
        ScrollPane sp = new ScrollPane(lblResult);
        
        
        // Layout
        HBox inp = new HBox();
        inp.getChildren().addAll(lbl, tfNumber, btnCalc);
        
        BorderPane bp = new BorderPane();
        bp.setTop(inp);
        bp.setCenter(sp);
        bp.setBottom(lblStatus);
        
        // Tooltip
        tfNumber.setTooltip(new Tooltip("Bitte geben sie den Namen eines Warframes ein"));
        btnCalc.setTooltip(new Tooltip("startet die ___________________"));


        // Szene und Fenster
        Scene scene = new Scene(bp, 400, 300);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Factors");
        primaryStage.show();
    }
    
    public void checkInput() {
        
        WikiScraper scraper = new WikiScraper();
        scraper.getWarframes();

        StringBuilder sb = new StringBuilder("Warframes: \n");
        for (String prime : WikiScraper.primes_List) {
            sb.append(prime + "\n");
            
        }
        lblResult.setText(sb.toString());

        String eingabe = tfNumber.getText();

        if(WikiScraper.primes_List.contains(eingabe)) {
            tfNumber.setStyle("");
            btnCalc.setDisable(false);
            tfNumber.setOnAction(handler);
            lblStatus.setText("");
        } else {
            tfNumber.setStyle("-fx-focus-color: red;");
            btnCalc.setDisable(true); // Button wird ausgegraut
            tfNumber.setOnAction(null); // auch enter funktionirt nicht
            lblStatus.setText("Bitte geben sie den Namen eines Warframes ein");
        }

    
}
}
