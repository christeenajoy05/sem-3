package com.example.sjcet.c5q2;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String dbname="user.db";
    private static final String tablename="user_table";
    private static final String col1="id";
    private static final String col2="name";
    private static final String col3="age";
    private static final String col4="mark";

    public DatabaseHelper( Context context) {
        super(context, dbname,null,1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String createTable="CREATE TABLE user_table("
                + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                +"name TEXT,"
                +"age INTEGER,"
                +"mark INTEGER)";
        db.execSQL(createTable);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS "+tablename);
        onCreate(db);
    }

    public boolean insertUser(String name, int age, int mark) {
        SQLiteDatabase db=this.getWritableDatabase();
        ContentValues contentValues=new ContentValues();
        contentValues.put(col2, name);
        contentValues.put(col3, age);
        contentValues.put(col4, mark);
        long result=db.insert(tablename,null,contentValues);
        return result!=-1;

    }


    public boolean updateUser(String name, int age, int mark) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(col3, age);
        contentValues.put(col4, mark);

        // Update all records (you might need to include a WHERE clause for specific updates)
        int updatedRows = db.update(tablename, contentValues, col2 + "=?", new String[]{name});
        return updatedRows > 0;

    }

    public boolean deleteUser(int id) {
        SQLiteDatabase db = this.getWritableDatabase();
        int result = db.delete(tablename, col1 + "=?", new String[]{String.valueOf(id)});
        return result > 0;

    }

    public Cursor getUserById(int id) {
        SQLiteDatabase db = this.getWritableDatabase();
        return db.rawQuery("SELECT * FROM " + tablename + " WHERE " + col1 + "=?", new String[]{String.valueOf(id)});

    }

    public Cursor getAllUsers() {
        SQLiteDatabase db = this.getWritableDatabase();
        return db.rawQuery("SELECT * FROM " + tablename, null);

    }
}
