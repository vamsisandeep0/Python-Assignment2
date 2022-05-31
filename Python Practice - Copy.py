{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "368aba36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bandra mumbai\n",
      "mumbai\n"
     ]
    }
   ],
   "source": [
    "text=\"bmaunmdbraai\"\n",
    "text1=text[0:len(text):2]\n",
    "text2=text[1:len(text):2]\n",
    "print(text1 +\" \" + text2)\n",
    "print(text2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d3aba52b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "string='yevqievbe7qnwqfggtbvq87vcaaahvuecviy'\n",
    "print(len(string))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d52a411f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "text\n"
     ]
    }
   ],
   "source": [
    "text='bb'\n",
    "print('text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5145d5be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "string='yevqievbe7qnwqfggtbvq87vcaaahvuecviy'\n",
    "print(len(string))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e703ff79",
   "metadata": {},
   "source": [
    "# Q1)Count the total number of orders [ Orders include both processed and returned orders] 63 66 ANS - 129 126 129"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5cb802d8",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4868/2531179296.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0minput_tuple\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Monty Python'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'British'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1969\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mlist1\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput_tuple\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "input_tuple=('Monty Python','British',1969)\n",
    "list1=list(input_tuple)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "35c0d8a8",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4868/926098911.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Monty Python'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'British'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1969\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mlist_new\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "input=('Monty Python','British',1969)\n",
    "list_new= list(input)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9456b4d5",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4868/2608192358.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mtuple_new\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m'Monty Python'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'British'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1969\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mlist_new\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtuple_new\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mlist_new\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Python'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mtuple_new2\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtuple\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist_new\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "tuple_new = ('Monty Python', 'British', 1969)\n",
    "list_new = list(tuple_new)\n",
    "list_new.append('Python')\n",
    "tuple_new2 = tuple(list_new)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "160caf68",
   "metadata": {},
   "outputs": [],
   "source": [
    "t1 = tuple_new + ('python',)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "289a3be7",
   "metadata": {},
   "outputs": [],
   "source": [
    "str='Kumar_Ravi_003'\n",
    "str1=str.split('_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "decec787",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['five', 'four', 'one', 'six', 'three', 'two']\n",
      "['one', 'two', 'three', 'four', 'five', 'six']\n"
     ]
    }
   ],
   "source": [
    "L = ['one','two','three', 'four', 'five', 'six']\n",
    "print(sorted(L))\n",
    "print (L)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ad3ddaba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['SAS', 'R', 'PYTHON', 'SPARK']\n"
     ]
    }
   ],
   "source": [
    "input_list=['SAS', 'R', 'PYTHON', 'SPSS']\n",
    "input_list[-1]='SPARK'\n",
    "print(input_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "55e8b3a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pythons syntax is easy to learn & Pythons syntax is very clear\n"
     ]
    }
   ],
   "source": [
    "a='Pythons syntax is easy to learn'\n",
    "b='Pythons syntax is very clear'\n",
    "c= a + ' & ' + b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cb12a26e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python\n"
     ]
    }
   ],
   "source": [
    "input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]\n",
    "a= input_list[2][0]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e4bf904e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Grapes', 'Orange', 'Strawberry']\n"
     ]
    }
   ],
   "source": [
    "A=['Orange','Grapes','Strawberry']\n",
    "A.sort()\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4c19e1dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Orange', 'Grapes', 'Strawberry']\n"
     ]
    }
   ],
   "source": [
    "A=['Orange','Grapes','Strawberry']\n",
    "sorted(A,reverse=True)\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b92db62e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Orange', 'Grapes', 'Strawberry']\n"
     ]
    }
   ],
   "source": [
    "A=['Orange','Grapes','Strawberry']\n",
    "sorted(A,reverse=False)\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1f1b15ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Grapes', 'Orange', 'Strawberry']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A=['Orange','Grapes','Strawberry']\n",
    "sorted(A, reverse=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4e2fc988",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted list:\n",
      "[1, 2, 3, 4, 5]\n",
      "\n",
      "Reverse sorted list:\n",
      "[5, 4, 3, 2, 1]\n",
      "[1, 2, 3, 4, 5]\n",
      "\n",
      "Original list after sorting:\n",
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "L = [1, 2, 3, 4, 5]\n",
    " \n",
    "print(\"Sorted list:\")\n",
    "print(sorted(L))\n",
    " \n",
    "print(\"\\nReverse sorted list:\")\n",
    "print(sorted(L, reverse = True))\n",
    "print(L)\n",
    " \n",
    "print(\"\\nOriginal list after sorting:\")\n",
    "print(L)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "77bc43d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 5, 3, 1]\n"
     ]
    }
   ],
   "source": [
    "A=[5,1,3,4,4,5,6,7]\n",
    "B=[3,3,5,5,1,7,2]\n",
    "Set1=set(A)\n",
    "Set2=set(B)\n",
    "C= Set1 & Set2\n",
    "print(sorted(C,reverse=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5b86e62f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Product Lead'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Employee_data = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}\n",
    "\n",
    "Employee_data.get(104)[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cbdeee54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Python': 40}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_1 = {\"Python\":40, \"R\":45}\n",
    "\n",
    "del dict_1[\"R\"]\n",
    "\n",
    "dict_1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "37d9c56d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['Python', 'R'])\n",
      "dict_values([40, 45])\n"
     ]
    }
   ],
   "source": [
    "d = {'Python':40, 'R':45}\n",
    "\n",
    "\n",
    "print(d.keys())\n",
    "print(d.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e08e005",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb234393",
   "metadata": {},
   "outputs": [],
   "source": [
    "From a Dictionary input_dict={'Name': 'Monty', 'Profession': 'Singer' }, get the value of a key based on user input which is not a part of the dictionary, in such a way that Python doesn't hit an error. If the key does not exist in the dictionary, Python should return 'NA'.\n",
    "\n",
    "Sample Input:\n",
    "\n",
    "{'Name': 'Monty', 'Profession': 'Singer' }\n",
    "\n",
    "Sample Output:\n",
    "\n",
    "NA\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "df346dd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NA\n"
     ]
    }
   ],
   "source": [
    "input_dict={'Name': 'Monty', 'Profession': 'Singer' }\n",
    "if \"Label\" in input_dict.keys():\n",
    "    print(input_dict[\"Label\"])\n",
    "else:\n",
    "    print(\"NA\") "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d39bf49",
   "metadata": {},
   "source": [
    "List of Values in a Dictionary.\n",
    "Description\n",
    "Create a SORTED list of all values from the dictionary input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}\n",
    "\n",
    "Sample Input:\n",
    "\n",
    "{'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}\n",
    "\n",
    "Sample Output:\n",
    "\n",
    "﻿['Amazon', 'Apple', 'RJIO', 'Twitter']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6b8077af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Amazon', 'Apple', 'RJIO', 'Twitter']"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}\n",
    "input_dict.values()\n",
    "sorted(input_dict.values())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc48e04a",
   "metadata": {},
   "source": [
    "# List of order ID’s which are processed \n",
    "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
    "\n",
    "# List of order ID’s which are returned\n",
    "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
    "\n",
    "# Consider the information available in the above two lists and answer the question given below"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "884f04d5",
   "metadata": {},
   "source": [
    "Count the total number of orders [ Orders include both processed and returned orders]\n",
    "63\n",
    "66\n",
    "126\n",
    "129"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6f5eb6ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bandra mumbai\n",
      "mumbai\n"
     ]
    }
   ],
   "source": [
    "text=\"bmaunmdbraai\"\n",
    "text1=text[0:len(text):2]\n",
    "text2=text[1:len(text):2]\n",
    "print(text1 +\" \" + text2)\n",
    "print(text2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "53c561f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178}\n",
      "129\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'new_returned_order' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_1856/1558116339.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[0mnew_processed_orders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msort_processed_orders\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msort_processed_orders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mnew_returned_orders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msort_returned_orders\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msort_returned_orders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew_processed_orders\u001b[0m \u001b[1;33m|\u001b[0m \u001b[0mnew_returned_order\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'new_returned_order' is not defined"
     ]
    }
   ],
   "source": [
    "processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]\n",
    "returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]\n",
    "total= (set(processed_orders) | set(returned_orders))\n",
    "print(total)\n",
    "print(len(total))\n",
    "sort_processed_orders=(sorted(processed_orders))\n",
    "sort_returned_orders=(sorted(returned_orders))\n",
    "new_processed_orders=sort_processed_orders[0:len(sort_processed_orders):2]\n",
    "new_returned_orders=sort_returned_orders[1:len(sort_returned_orders):2]\n",
    "print(new_processed_orders | new_returned_order)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df77f1f1",
   "metadata": {},
   "source": [
    "Calculate the mean age of the employees\n",
    "31.36\n",
    "36.48\n",
    "28.77\n",
    "32.47"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "fa5c2868",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_1856/3096241882.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mEmployee_data\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m101\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m102\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m103\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m104\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m31\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m105\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m26\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m106\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m107\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m108\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m109\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m110\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m111\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m112\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m113\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m115\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m116\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m117\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m118\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m119\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m120\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m121\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m122\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m39\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m123\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m124\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m125\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m126\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m127\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m40\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m128\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m129\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m130\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m131\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m37\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m132\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m133\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m36\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m134\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m135\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m136\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m137\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m138\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m139\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m140\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m39\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m141\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m142\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m143\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m39\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m145\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m34\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m146\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m26\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m147\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m148\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m38\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m149\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m150\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m24\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m151\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m152\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m34\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m153\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m154\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m155\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m156\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m31\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m158\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m160\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m161\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m162\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m163\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m24\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m164\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m166\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m24\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m167\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m168\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m169\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m170\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m34\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m171\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m37\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m172\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m173\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m35\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m174\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m175\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m44\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m176\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m177\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m178\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m26\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m179\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msum\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mEmployee_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mEmployee_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not callable"
     ]
    }
   ],
   "source": [
    "Employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27}\n",
    "print(sum(Employee_data.values()))\n",
    "print(len(Employee_data.values()))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "bf5d46dc",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_1856/2482486456.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mEmployee_data\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m101\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m102\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m103\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m104\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m31\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m105\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m26\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m106\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m107\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m108\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m109\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m110\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m111\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m112\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m113\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m115\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m116\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m117\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m118\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m119\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m120\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m121\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m122\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m39\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m123\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m124\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m125\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m43\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m126\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m127\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m40\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m128\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m129\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m130\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m131\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m37\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m132\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m133\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m36\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m134\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m135\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m136\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m137\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m138\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m139\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m140\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m39\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m141\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m142\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m143\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m39\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m145\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m34\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m146\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m26\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m147\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m148\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m38\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m149\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m150\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m24\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m151\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m152\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m34\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m153\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m154\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m29\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m155\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m156\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m31\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m158\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m25\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m160\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m161\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m162\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m163\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m24\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m164\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m166\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m24\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m167\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m28\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m168\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m169\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m170\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m34\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m171\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m37\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m172\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m45\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m173\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m35\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m174\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m23\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m175\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m44\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m176\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m177\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m30\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m178\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m26\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m179\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m27\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mEmployee_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not callable"
     ]
    }
   ],
   "source": [
    "Employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27}\n",
    "print(len(Employee_data.values()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "643815e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\tally'"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c91ab97d",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=int(input(\"enter\"))\n",
    "if x%2==0 :\n",
    "    print(\"x is even\")\n",
    "else :\n",
    "    print('x is odd')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "87c4f545",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'lower'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10020/1073510018.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'VARMA'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'raj'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Gupta'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'SaNdeeP'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0minput\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'list' object has no attribute 'lower'"
     ]
    }
   ],
   "source": [
    "input=['VARMA','raj','Gupta','SaNdeeP']\n",
    "input.lower()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd018750",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
