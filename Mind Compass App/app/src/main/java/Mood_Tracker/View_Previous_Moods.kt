package Mood_Tracker

import android.content.Context
import android.graphics.Color
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Gravity
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.view.marginTop
import com.example.Main.*

import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue
import com.github.kittinunf.fuel.Fuel
import com.github.kittinunf.fuel.core.extensions.jsonBody
import com.github.kittinunf.fuel.json.responseJson
import kotlinx.android.synthetic.main.activity_medication.*
import kotlinx.android.synthetic.main.activity_view__previous__moods.*

import java.util.*
import kotlin.collections.ArrayList

class View_Previous_Moods : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_view__previous__moods)



        var userName = intent.getStringExtra("UserName")

        var resp: String = AsyncGET(this,userName).execute().get()

        var tempMoodArray:ArrayList<tempMoods> = ArrayList<tempMoods>()

        var moodArray:ArrayList<String> = ArrayList<String>()
        var timeArray:ArrayList<String> = ArrayList<String>()
        var descArray:ArrayList<String> = ArrayList<String>()
        var txtViewArray:ArrayList<TextView> = ArrayList<TextView>()

        var test:String = ""

        val tokenizer: StringTokenizer = StringTokenizer(resp)
                    while(tokenizer.hasMoreTokens())
                    {
                        var compare:String = tokenizer.nextToken()

                                var tempmood:String = ""
                                var tempTime:String = ""
                                var tempDesc:String = ""

                                if(compare == "{"+'"'+"name"+'"'+":")
                                {

                                    tempmood = tokenizer.nextToken().replace("},","")
                                    moodArray.add(tempmood)

                                }else if(compare == '"'+"logged_time"+'"'+":")
                                {
                                    tempTime = tokenizer.nextToken().replace(",","")
                                    timeArray.add(tempTime)

                                }else if(compare == '"'+"description"+'"'+":")
                                {
                                    var tempContains:String = tokenizer.nextToken()

                                    while(!tempContains.contains("}"))
                                    {
                                        tempDesc= tempDesc+" "+tempContains
                                        tempContains = tokenizer.nextToken()
                                    }
                                    descArray.add(tempDesc)
                                }
//                                var tempMood:tempMoods = tempMoods(tempmood,tempTime,tempDesc)
//                                tempMoodArray.add(tempMood)


                    }

            for( i in moodArray.indices)
        {
          var textView = TextView(this)
            textView.setText("Mood: "+ "${moodArray[i]}\n"+
                            "Description: "+ "${descArray[i]}\n"+
                            "Date: "+ "${timeArray[i]}\n")

            textView.textSize = 20f
            textView.setBackgroundColor(Color.LTGRAY)

            txtViewArray.add(textView)

        }
        var textView = TextView(this)
        textView.textSize = 35f
        textView.setText("Previous Moods")
        textView.gravity = Gravity.CENTER
        linearLayout.addView(textView)
        for(i in txtViewArray)
        {
            linearLayout.addView(i)
        }
    }
}



private class AsyncGET(private val context: Context, val name:String) : AsyncTask<String, Void, String>()
{


    var userName = name


    override fun doInBackground(vararg params: String?): String {



        val (request, response, result) = Fuel.get("http://10.0.2.2:8000/api/mood/$userName").responseString()
        val (data, error)= result
        println(request.toString())
        println("response:::"+response.toString())
        println("result:::"+result.toString())
        println("data:::"+data)


        return data.toString()
    }

    override fun onPostExecute(result: String?) {
        super.onPostExecute(result)


    }


}
data class tempMoods(val mood:String,val time:String, val desc:String)