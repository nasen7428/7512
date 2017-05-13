package com.example.cat.a7512_android.view;

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import com.example.cat.a7512_android.R;

/**
 * Created by cat on 2017/5/12.
 */
public class NodeView extends LinearLayout {
    public NodeView(Context context) {
        super(context);
        create(context);
    }

    public NodeView(Context context, AttributeSet attrs) {
        super(context, attrs);
        create(context);
    }

    public NodeView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        create(context);
    }

    Button bAddInput,bAddOutput,bEdit;
    TextView tTitle,tDetial;

    private void create(Context context) {
        LayoutInflater.from(context).inflate(R.layout.node_edit,this);
        bAddInput = (Button) findViewById(R.id.button_add_input);
        bAddOutput = (Button) findViewById(R.id.button_add_output);
        bEdit = (Button) findViewById(R.id.button_edit_text);
        tTitle = (TextView) findViewById(R.id.textView_title);
        tDetial = (TextView) findViewById(R.id.textView_detial);
        showEditType(false);
        setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                showEditType(true);
            }
        });
    }

    /**
     * 编辑模式切换
     * @param isshow
     */
    private void showEditType(boolean isshow) {
        if (isshow) {
            bEdit.setVisibility(VISIBLE);
            bAddOutput.setVisibility(VISIBLE);
            bAddInput.setVisibility(VISIBLE);
        }else{
            bEdit.setVisibility(GONE);
            bAddInput.setVisibility(GONE);
            bAddOutput.setVisibility(GONE);
        }
    }

}
