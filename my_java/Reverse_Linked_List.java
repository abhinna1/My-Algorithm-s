package my_java;
import java.io.*;
import java.util.*;


class SingelyLinkedList{
    Node head;
    Node tail;
    public SingelyLinkedList(){
        head = null;
        tail = null;
    }

    public void insertNode(int data){
        if (head==null){
            head = tail = new Node(data);
        }
        else{
            Node temp = new Node(data);
            tail.next = temp;
            tail = temp;
        }
    }

    public Node reverse(){
        Node current = head;
        Node next = null;
        Node prev = null;
        while(current!=null){
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        return prev;
    }

    public void printList(){
        Node temp = head;
        while(temp!=null){
            System.out.println(temp.data);
            temp = temp.next;
        }
    }
}

class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = null;
    }
}

class Reverse_Linked_List{
    public void execute(){
        SingelyLinkedList list = new SingelyLinkedList();
        list.insertNode(1);
        list.insertNode(2);
        list.insertNode(3);
        list.insertNode(4);
        // Now reverse the list.
        Node new_head = list.reverse();
        Node temp = new_head;
        while(temp!=null){
            System.out.println(temp.data);
            temp=temp.next;
        }

    }
    public static void main(String[] args) {
        new Reverse_Linked_List().execute();

    }
}