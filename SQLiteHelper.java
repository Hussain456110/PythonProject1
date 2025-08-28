import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class SQLiteHelper {
    public static void main(String[] args) {
        String dbURL = "jdbc:sqlite:balancebuddy.db"; // database file will be created

        try (Connection conn = DriverManager.getConnection(dbURL)) {
            if (conn != null) {
                System.out.println("✅ Connection to SQLite has been established.");
            }
        } catch (SQLException e) {
            System.out.println("❌ Database connection failed:");
            e.printStackTrace();
        }
    }
}
javac -cp ".;sqlite-jdbc-3.43.0.0.jar" SQLiteHelper.java
java -cp ".;sqlite-jdbc-3.43.0.0.jar" SQLiteHelper
java -cp ".:sqlite-jdbc-3.43.0.0.jar" SQLiteHelper



