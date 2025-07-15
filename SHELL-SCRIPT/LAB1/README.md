# lab1 #
# Using sed utility # 
## **📌1- Display the lines that contain the word “lp” in /etc/passwd file.**
📸![Alt text](assets/pic1.png)

## **📌2-Display /etc/passwd file except the third line.**
📸![Alt text](assets/pic2.png)

## **📌3-Display /etc/passwd file except the last line.** 
📸![Alt text](assets/pic3.png)

## **📌4-Display /etc/passwd file except the lines that contain the word “lp”.** 
📸![Alt text](assets/pic4.png)
## **📌5-Substitute all the words that contain “lp” with “mylp” in /etc/passwd file.** 
![Alt text](assets/pic5.png)

# Using awk utility # 

## **📌1-Print full name (comment) of all users in the system.** 
![Alt text](assets/pic6.png)

## **📌2-Print login, full name (comment) and home directory of all users.( Print each line preceded** 
![Alt text](assets/pic7.png)
## **📌3-Print login, uid and full name (comment) of those uid is greater than 500** 
![Alt text](assets/pic8.png)

## **📌4-Print login, uid and full name (comment) of those uid is exactly 500**
![Alt text](assets/pic9.png)
 **📌5-Print line from 5 to 15 from /etc/passwd**
![Alt text](assets/pic10.png)
or 
awk -F: '
{
      if(NR >=5 && NR <=15)
      print $0
}
' /etc/passwd
## **📌6-Change lp to mylp**
![Alt text](assets/pic15.png)
or 
awk -F: '
{
  i=i
  while(i <= NF){
    if($i == "lp"){
      $i == "mylp"  
    }
    i++;
  }  
}
'

## **📌7-Print all information about greatest uid.**
![Alt text](assets/pic11.png)

![Alt text](assets/pic12.png)
## **📌8-Get the sum of all accounts id’s.**
![Alt text](assets/pic13.png)
![Alt text](assets/pic14.png)


