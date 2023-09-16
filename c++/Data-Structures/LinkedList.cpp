# include <iostream>

using namespace std;
class Node{
    public:
        int value;
        Node *next;

        Node(int value){
            this->value=value;
            this->next=NULL;
        }
};
class LinkedList{
    
    public:
        Node* head;
        LinkedList(){
            this->head = NULL;
        }

        void insert_node(int value){
            Node * newNode = new Node(value);

            if(this->head == NULL){
                this-> head = newNode;
            }
            else{
                Node * temp = head;
                while(temp->next!=NULL){
                    temp = temp->next;
                }
                temp->next = newNode;
            }
        }

        void print_list(){
            Node * temp = head;
            while (temp!=NULL){
                cout << temp->value << endl;
                temp = temp->next;
            }
        }
};

int main(){
    LinkedList lList = LinkedList();
    lList.insert_node(1);
    lList.insert_node(2);
    lList.insert_node(3);

    lList.print_list();
    cout << endl;
    cout << "head: " << lList.head->value << endl;

    // cout << lList.head->value;

    return 0;
}