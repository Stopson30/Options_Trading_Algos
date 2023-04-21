using iTextSharp.text;
using iTextSharp.text.pdf;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        // Replace these values with your own
        string inputFile = "input.pdf";
        string outputFile = "output.pdf";
        string password = "myPassword";

        // Create a reader object to read the input file
        PdfReader reader = new PdfReader(inputFile);

        // Create an output stream to write the encrypted PDF to
        using (FileStream outputStream = new FileStream(outputFile, FileMode.Create, FileAccess.Write))
        {
            // Create an encryption object with the desired password
            PdfEncryptor encryptor = new PdfEncryptor(
                PdfWriter.VERSION_1_5,
                outputStream,
                Encoding.ASCII.GetBytes(password),
                null,
                PdfWriter.ALLOW_PRINTING);

            // Set the encryption options
            encryptor.SetEncryption(
                PdfWriter.STRENGTH128BITS,
                PdfWriter.ENCRYPTION_AES_128,
                PdfWriter.ALLOW_PRINTING,
                PdfWriter.ENCRYPTION_AES_128);

            // Copy the input PDF to the output stream, encrypting it in the process
            PdfCopy copy = new PdfCopy(encryptor, outputStream);
            encryptor.SetFullCompression();
            copy.SetMergeFields();
            outputStream.SetLength(0);

            for (int i = 1; i <= reader.NumberOfPages; i++)
            {
                copy.AddPage(copy.GetImportedPage(reader, i));
            }

            // Close the output stream and reader
            reader.Close();
            outputStream.Close();
        }
    }
}

Main();sxf 

