package Mood_Tracker

import android.content.Context
import android.os.AsyncTask


import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.*


import com.example.Main.R
import com.github.kittinunf.fuel.Fuel
import com.github.kittinunf.fuel.core.extensions.jsonBody
import kotlinx.android.synthetic.main.activity_mood__input.*
import java.time.Instant
import java.time.ZoneOffset


import java.time.format.DateTimeFormatter


class Mood_Input : AppCompatActivity() {




    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_mood__input)

        var userName = intent.getStringExtra("UserName")
        var mood = intent.getStringExtra("Mood")
        var txtDescription = findViewById(R.id.txt_userDescription) as EditText
        var btnSubmit = findViewById(R.id.btnAddMood) as Button




        val emotionImageView = ImageView(this)
        emotionImageView.layoutParams = LinearLayout.LayoutParams(170,170)
        emotionImageView.x = 300F
        emotionImageView.y = 300F

        if(mood.equals("Happy"))
        {
            val emoticonImage = R.drawable.ic_emoticon_happy_outline
            var resID = emoticonImage
            emotionImageView.setImageResource(resID)
            val layout = findViewById<RelativeLayout>(R.id.moodInputRelativeLayout)
            layout?.addView(emotionImageView)


        }else if(mood.equals("Sad"))
        {
            val emoticonImage = R.drawable.ic_emoticon_sad_outline
            var resID = emoticonImage
            emotionImageView.setImageResource(resID)
            val layout = findViewById<RelativeLayout>(R.id.moodInputRelativeLayout)
            layout?.addView(emotionImageView)


        }else if(mood.equals("Excellent"))
        {
            val emoticonImage = R.drawable.ic_emoticon_excited_outline
            var resID = emoticonImage
            emotionImageView.setImageResource(resID)
            val layout = findViewById<RelativeLayout>(R.id.moodInputRelativeLayout)
            layout?.addView(emotionImageView)


        }else if(mood.equals("Meh"))
        {
            val emoticonImage = R.drawable.ic_emoticon_neutral_black_24dp
            var resID = emoticonImage
            emotionImageView.setImageResource(resID)
            val layout = findViewById<RelativeLayout>(R.id.moodInputRelativeLayout)
            layout?.addView(emotionImageView)


        }else if(mood.equals("Angry"))
        {
            val emoticonImage = R.drawable.ic_emoticon_angry_outline
            var resID = emoticonImage
            emotionImageView.setImageResource(resID)
            val layout = findViewById<RelativeLayout>(R.id.moodInputRelativeLayout)
            layout?.addView(emotionImageView)


        }

        btnAddMood.setOnClickListener{
            val desc = txtDescription.text.toString()
            var loggedTime: String = DateTimeFormatter.ISO_INSTANT.format(Instant.now())

            AsyncPOST(this,mood,desc,userName, loggedTime).execute()
            Toast.makeText(this, "Mood Added to Database", Toast.LENGTH_LONG).show()

        }





    }

}
private class AsyncPOST(private val context: Context, val mood:String, val desc:String, val name:String,val time:String) : AsyncTask<String, Void, String>()
{




    var userMood = mood
    var userName = name


    override fun doInBackground(vararg params: String?): String {

        val bodyJson = """
            {
            "generic_mood" : "$userMood",
            "logged_time": "$time",
            "description" : "$desc"
            }"""
     //   2020-05-26T21:28:44.405000Z
        val (request, response, result) = Fuel.post("http://10.0.2.2:8000/api/mood/$userName/add").jsonBody(bodyJson).responseString()

        println(request.toString())
        println(response.toString())
        println(result.toString())







        return name
    }


}