package Medication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.Main.R
import com.ms.square.android.expandabletextview.ExpandableTextView

class Medication : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_medication)

        val expTv: ExpandableTextView = findViewById(R.id.expand_text_view)
        expTv.setText("Medication 1 \n" +
                "Dosage: Dosage instructions\n"
                +"Description: This is where the Description of the medication will go as it will be long ive made this longer than is neccessary")

        val expTv2: ExpandableTextView = findViewById(R.id.expand_text_view2)
        expTv2.setText("Medication 2 \n" +
                "Dosage: Dosage instructions\n"
                +"Description: This is where the Description of the medication will go as it will be long ive made this longer than is neccessary")

        val expTv3: ExpandableTextView = findViewById(R.id.expand_text_view3)
        expTv3.setText("Medication 3 \n" +
                "Dosage: Dosage instructions\n"
                +"Description: this is giberish and just a place holder for testing purposes ahgfdkjhaf kkjhfkj asfkja jfjjf;ajfladflk;akjgfkjhkhfashfkafkakfhka  khafdkj hkjhkj kjhaa hkjahg kj;hgkjha kjghkjhkjah kjafkj;akjakjhjfljkakjhgkjakjhahkhkafka")

    }
}
