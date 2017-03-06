/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package paquete;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.Scanner;
import java.util.logging.Level;
import javax.swing.JOptionPane;
/**
 *
 * @author HP
 */
class opmatrizd {
     public static OkHttpClient webClient = new OkHttpClient();
     String agregar(String text) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato1", text)
                .build();
       return  enviardato("matrizagregar", formBody);
       // String r = getString("listasm", formBody); 
       // System.out.println(r + "---");
    }
     String buscar(String text) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato1", text)
                .build();
       return  enviardato("listasb", formBody);
       // String r = getString("listasm", formBody); 
       // System.out.println(r + "---");
    }
        
        void buscarletra(String text) {
           RequestBody formBody = new FormEncodingBuilder()
                .add("dato1", text)
                .build();
         String tam = enviardato("matrizbletra", formBody);
         //System.out.println(tam);
         System.out.println("Datos");
            for (int i = Integer.parseInt(tam)-1; i >= 0; i--) {
           RequestBody formBody1 = new FormEncodingBuilder()
                .add("dato1", text)
                .add("dato2",String.valueOf(i) )
                .build();
     
         String mos = enviardato("matrizbletra1", formBody1);
                System.out.print(mos+"  ");
                
            }
        //JOptionPane.showMessageDialog(null, tam);
        }

    void buscardir(String text) {
        System.out.println();
     RequestBody formBody = new FormEncodingBuilder()
                .add("dato1", text)
                .build();
         String tam = enviardato("matrizbdir", formBody);
         //System.out.println(tam);
         System.out.println("Datos");
            for (int i = Integer.parseInt(tam)-1; i >= 0; i--) {
           RequestBody formBody1 = new FormEncodingBuilder()
                .add("dato1", text)
                .add("dato2",String.valueOf(i) )
                .build();
     
         String mos = enviardato("matrizbdir1", formBody1);
                System.out.print(mos+"  ");
                
            }
            System.out.println();
    
    
    }
	

    private String enviardato(String metodo, RequestBody formBody) {
              try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
           String response_string = response.body().string();//y este seria el string de las respuesta
             // System.out.println("entr");
          return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(paquete.opmatrizd.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(paquete.opmatrizd.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }




}
