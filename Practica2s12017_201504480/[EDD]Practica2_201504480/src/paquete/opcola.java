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
/**
 *
 * @author HP
 */
class opcola {
     public static OkHttpClient webClient = new OkHttpClient();
     String queue(String text) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato1", text)
                .build();
       return  enviardato("colaq", formBody);
       // String r = getString("listasm", formBody); 
       // System.out.println(r + "---");
    }
     String dequeue() {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato1", "")
                .build();
        String enviar = enviardato("coladq", formBody);
         System.out.println(enviar);
       return  enviar;
       
       // String r = getString("listasm", formBody); 
       // System.out.println(r + "---");
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
            java.util.logging.Logger.getLogger(paquete.opcola.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(paquete.opcola.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }


}
