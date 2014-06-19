import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.io.File;
import java.util.ArrayList;
 
public class File2Clip {
 
    public static void main(String[] args) {
 
        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
        
        //File file = new File("C:\\Users\\Saurabh\\Documents\\Visual Studio 2013\\Projects\\File2Clip\\File2Clip\\bin\\x86\\Release\\File2Clip.exe");
        ArrayList<File> list = new ArrayList<File>();
        
        for (int index = 0; index < args.length; ++index)
        {
        	File file = new File(args[index]);
        	list.add(file);
            //System.out.println("args[" + index + "]: " + args[index]);
        }
        
        ClipboardFiles clipboardFiles = new ClipboardFiles(list);
 
        clipboard.setContents(clipboardFiles, clipboardFiles);
 
    }
 
}