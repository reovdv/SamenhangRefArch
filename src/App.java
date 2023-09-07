import java.io.IOException;

public class App {
    public static void main(String[] args) {
        try {
            // Specify the path to the JAR file you want to execute
            String jarFilePath = "archimate2rdf.jar";

            // Specify the input and output XML files
            String inputXmlFile = "C:/Users/remco/Documents/GitHub/SamenhangRefArch/SamenhangRefArch/referentiearchitecturen/FORA.xml";
            String outputXmlFile = "C:/Users/remco/Documents/GitHub/SamenhangRefArch/SamenhangRefArch/referentiearchitecturen_rdf/FORA_rdf.xml";

            // Create a ProcessBuilder to run the JAR file with input and output parameters
            ProcessBuilder processBuilder = new ProcessBuilder("java", "-jar", jarFilePath, inputXmlFile, outputXmlFile);

            // Start the process
            Process process = processBuilder.start();

            // Wait for the process to complete (optional)
            int exitCode = process.waitFor();

            // Print the exit code (0 indicates success)
            System.out.println("Exit code: " + exitCode);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}