/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio12042024;

/**
 *
 * @author laort
 */
public class persona {

    private String nombre;
    private int edad;
    private String direccion;
    private String telefono;
    private String email;
    private String genero;
    private String profesion;

    public persona(){
    
    }

    public persona(String nombre, int edad, String direccion, String telefono, String email, String genero, String profesion) {
        this.nombre = nombre;
        this.edad = edad;
        this.direccion = direccion;
        this.telefono = telefono;
        this.email = email;
        this.genero = genero;
        this.profesion = profesion;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getProfesion() {
        return profesion;
    }

    public void setProfesion(String profesion) {
        this.profesion = profesion;
    }

    public static void main(String[] args) {
        persona persona = new persona("Luis", 19, "Tacuba 26", "5545606548", "laortegasal@gmail.com", "Masculino", "Ingeniero");
        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Edad: " + persona.getEdad());
        System.out.println("Direccion: " + persona.getDireccion());
        System.out.println("Telefono: " + persona.getTelefono());
        System.out.println("Email: " + persona.getEmail());
        System.out.println("Genero: " + persona.getGenero());
        System.out.println("Profesion: " + persona.getProfesion());
    }
    
}

