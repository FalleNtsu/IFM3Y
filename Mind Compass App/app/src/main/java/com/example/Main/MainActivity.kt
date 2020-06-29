package com.example.Main

import Medication.Medication
import Mood_Tracker.MoodTracker
import User_Activities.Activities_Screen
import android.content.Context

import android.content.Intent
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable

import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import android.view.MenuItem
import android.view.View
import android.widget.MultiAutoCompleteTextView
import androidx.appcompat.widget.Toolbar
import androidx.drawerlayout.widget.DrawerLayout
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.core.view.GravityCompat

import com.github.kittinunf.fuel.Fuel


import com.github.kittinunf.fuel.core.extensions.jsonBody
import com.google.android.material.navigation.NavigationView
import kotlinx.android.synthetic.main.content_main.*


class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener
{
    var loggedIn = false
    var resp = ""
    var userName = ""

    //below for the nav bar
    lateinit var toolbar: Toolbar
    lateinit var drawerLayout: DrawerLayout
    lateinit var navView: NavigationView

    //actualy starts the app
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // get reference to all views
        var txt_userName = findViewById(R.id.txt_userName) as EditText
        var txt_userPassword = findViewById(R.id.txt_userPassword) as EditText
        var btn_reset = findViewById(R.id.btn_reset) as Button
        var btn_submit = findViewById(R.id.btn_submit) as Button
        var btn_register = findViewById(R.id.btn_register) as Button

        //FOR TOOl bar
        toolbar = findViewById(R.id.toolbar)
        setSupportActionBar(toolbar)

        drawerLayout = findViewById(R.id.drawer_layout)
        navView = findViewById(R.id.nav_view)

        val toggle = ActionBarDrawerToggle( this, drawerLayout, toolbar, 0, 0)
        drawerLayout.addDrawerListener(toggle)
        toggle.syncState()
        navView.setNavigationItemSelectedListener(this)

        btn_reset.setOnClickListener {
            // clearing user_name and password edit text views on reset button click
            txt_userName.setText("")
            txt_userPassword.setText("")
        }

        // set on-click listener
        btn_submit.setOnClickListener {
            val user_name = txt_userName.text;
            userName = user_name.toString()
            val password = txt_userPassword.text;
            Toast.makeText(this@MainActivity, user_name, Toast.LENGTH_LONG).show()

            // CODE for user validation



           resp = AsyncGet(this,user_name.toString(),password.toString()).execute().get()
            if (resp == "t")
            {
                loggedIn = true
            }

            if(loggedIn)
            {
                logInLayout.visibility = View.INVISIBLE
            }
        }




        //set on click listener for register
        btn_register.setOnClickListener(){
            val intent = Intent(this, Register::class.java)
            startActivity(intent)


        }

    }
    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.nav_profile -> {

                Toast.makeText(this, "Profile clicked", Toast.LENGTH_SHORT).show()

            }
            R.id.nav_medication -> {
                Toast.makeText(this, "Medication clicked", Toast.LENGTH_SHORT).show()
                val medicationIntent = Intent(this, Medication::class.java)

                startActivity(medicationIntent)

            }
            R.id.nav_mood_tracking -> {
                Toast.makeText(this, "Mood Tracking clicked", Toast.LENGTH_SHORT).show()
                val moodIntent = Intent(this, MoodTracker::class.java)
                moodIntent.putExtra("UserName","$userName")
                startActivity(moodIntent)
            }
            R.id.nav_update -> {
                Toast.makeText(this, "Update clicked", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_logout -> {
                Toast.makeText(this, "Sign out clicked", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_activities -> {
                Toast.makeText(this, "Activities clicked", Toast.LENGTH_SHORT).show()
                val activitesIntent = Intent(this, Activities_Screen::class.java)
                startActivity(activitesIntent)
            }
        }
        drawerLayout.closeDrawer(GravityCompat.START)
        return true
    }
}

private class AsyncGet(private val context:Context, val name:String, val pass:String) : AsyncTask<String, Void, String>()
{
    var login = "f"


    override fun doInBackground(vararg params: String?): String {
        val bodyJson = """
            {
            "username" : "$name",
            "password" : "$pass"
            }"""
        var testTemp: com.github.kittinunf.fuel.core.Response? = null;
        Fuel.post("http://10.0.2.2:8000/api/user/login").jsonBody(bodyJson).responseString() { request, response, result ->
            val (data, error)= result
            testTemp = response
            val datastring =""""""+data.toString()+""""""
            result.fold(
                {
                    //Success

                    println("request:::::"+request)
                    println("response::::"+response)
                    println("result::::"+result.toString())
                    println("data:::"+data.toString())

                    val compare = data.toString()

                    if(compare.contains("Login Successful"))
                    {
                        login = "t"
                    }
//                    val mapper = jacksonObjectMapper()
//                    var logindata : LogInDataClass = mapper.readValue<LogInDataClass>(datastring)
//
//                    println("logInData"+logindata.toString())
//                    val tokenizer: StringTokenizer = StringTokenizer(data)
//                    while(tokenizer.hasMoreTokens())
//                    {
//                        if(tokenizer.nextToken()=="true,")
//                        {
//                            login = "true"
//                        }
//                        println(tokenizer.nextToken())
//                    }


                },{

                    //Failure
                    Toast.makeText(context, error.toString(),Toast.LENGTH_LONG)
                })


        }

//        val temp = result
//        val temp1 = response.body()
//        println("request"+ request.toString())
//        println("result"+ temp.toString())
//        println("response" +temp1)

//        val (success, message) = result
//        if(success != null) {println(success.find { true })}
//        println("payload" + success.get(0))



//        val logInDataClass : LogInDataClass;
//        val JsonResponse: JSONObject = JSONObject()
//        var jsonArray_Data : JSONArray = JsonResponse.getJSONArray("Body")
//        println(jsonArray_Data.toString())


        return login
    }
    override fun onPostExecute(result: String?) {
        super.onPostExecute(result)


    }

}
