import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.Enumeration;

public class ZipExtractor {

    public static void unzip(String zipfile, String destinationDirectory){
        // Unzip zipFile into destinationDirectory
        try {
            ZipFile zipFile = new ZipFile(zipfile);
            Enumeration<? extends ZipEntry> entries = zipFile.entries();
            while(entries.hasMoreElements()){
                ZipEntry entry = entries.nextElement();
                File entryDestination = new File(destinationDirectory,  entry.getName());

                // validate the entryDestination is not vulnerable to Zip Slip attack
                if (!entryDestination.getCanonicalPath().startsWith(destinationDirectory)){
                    throw new IOException("Entry is outside of the target dir: " + entry.getName());
                }

                if (entry.isDirectory()){
                    entryDestination.mkdirs();
                } else {
                    entryDestination.getParentFile().mkdirs();
                    InputStream in = zipFile.getInputStream(entry);
                    OutputStream out = new FileOutputStream(entryDestination);
                    byte[] buffer = new byte[1024];
                    int len;
                    while((len = in.read(buffer)) >= 0){
                        out.write(buffer, 0, len);
                    }
                    in.close();
                    out.close();
                }
            }
            zipFile.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}