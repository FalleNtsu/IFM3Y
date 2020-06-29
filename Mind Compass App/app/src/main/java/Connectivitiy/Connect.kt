package Connectivitiy

import android.os.AsyncTask
import com.github.kittinunf.fuel.Fuel

class Connect()
{

}



class AsyncGet : AsyncTask<String, Void, String>()
{
//    val UserName = Username;
//    val Pasword ;

    override fun doInBackground(vararg params: String?): String {
        val bodyJson = """
            {
            "username" : "a",
            "password" : "a"
            }"""
        val  (request, response, result) = Fuel.post("http://10.0.2.2:8000/api/user/login").body(bodyJson).response()

        val temp = result
        val temp1 = response
        println("request"+ request.toString())
        println("result"+ temp.toString())
        println("response" +temp1.toString())

        return response.toString()
    }

}