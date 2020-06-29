package Mood_Tracker

import User_Activities.Activities_Screen
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MenuItem
import android.widget.Button
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.widget.Toolbar
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import com.example.Main.R
import com.google.android.material.navigation.NavigationView

class MoodTracker : AppCompatActivity() {

 var usernamePassOn = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_mood_tracker)
        val userName = intent.getStringExtra("UserName")
        usernamePassOn = userName

        var btnPreviousMoods = findViewById(R.id.btn_previous_moods) as Button

        //set images as buttons
        val happyEmoticon = findViewById(R.id.happyEmoticon) as ImageView
        val excellentEmoticom = findViewById(R.id.excellentEmoticon) as ImageView
        val angryEmoticon = findViewById(R.id.angryEmoticon) as ImageView
        val sadEmoticon = findViewById(R.id.sadEmoticon) as ImageView
        val mehEmoticon = findViewById(R.id.mehEmoticon) as ImageView

        var userMood:String
        //set image on click listners
        happyEmoticon.setOnClickListener {
        userMood = "Happy"
            inputMood(userMood)

        }

        excellentEmoticom.setOnClickListener {
            userMood = "Excellent"
            inputMood(userMood)
        }

        angryEmoticon.setOnClickListener {
            userMood = "Angry"
            inputMood(userMood)
        }

        sadEmoticon.setOnClickListener {
            userMood = "Sad"
            inputMood(userMood)
        }

        mehEmoticon.setOnClickListener {
            userMood = "Meh"
            inputMood(userMood)
        }

        btnPreviousMoods.setOnClickListener{
            val PreviousMoodIntent = Intent(this, View_Previous_Moods::class.java)
            PreviousMoodIntent.putExtra("UserName", usernamePassOn)
            startActivity(PreviousMoodIntent)
        }
    }


    fun inputMood(mood:String)
    {
        val MoodInputIntent = Intent(this, Mood_Input::class.java)
        MoodInputIntent.putExtra("Mood", mood)
        MoodInputIntent.putExtra("UserName", usernamePassOn)
        startActivity(MoodInputIntent)
    }
}
