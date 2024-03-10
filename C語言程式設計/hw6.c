#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include <stdlib.h>
#define Maxscore 100
int idx=0;
int atoi ( const char * str );
void del(char input[1],int del,int len)
{
    int i=0;
    for (; i<strlen(input)-len-del; i++)
    {
        input[del+i]=input[len+del+i];
    }
    input[del+(strlen(input)-len-del)]='\0';

}
char *getword(char *text, char *word) {
    char *ptr = text;
    char *qtr = word;
    while (*ptr && isspace(*ptr)) {ptr++;}
    while (*ptr && !(isspace(*ptr))) {
        if (qtr-word >= 128) {
            fprintf(stderr,"word length 太長\n");
            break;
        }
        *qtr++=*ptr++;
    }
    *qtr = '\0';
    if (qtr-word==0) {
        return NULL;
    }
    return ptr;
}
void insert(char ** input,int number ,char **name,char **math,char **english, char **program) {
    int i;
    del(input[1],0,2);
    strcpy(name[idx],input[1]);
    for (i=2;i<number;i++) {
        if (input[i][0]=='m') {
            del(input[i],0,2);
            if (atoi(input[i])>=0 && atoi(input[i]) < 101) {
                if (input[i][0]=='+') {
                    del(input[i],0,1);
                }
                strcpy(math[idx],input[i]);
            }
        }
        if (input[i][0]=='e') {
            del(input[i],0,2);
            if (atoi(input[i])>=0 && atoi(input[i]) < 101) {
                if (input[i][0]=='+') {
                    del(input[i],0,1);
                }
                strcpy(english[idx],input[i]);
            }
        }
        if (input[i][0]=='p') {
            del(input[i],0,2);
            if (atoi(input[i])>=0 && atoi(input[i]) < 101) {
                if (input[i][0]=='+') {
                    del(input[i],0,1);
                }
                strcpy(program[idx],input[i]);
            }
        }
    }
    if (strcmp(math[idx],"\0")==0) strcpy(math[idx],"-1");
    if (strcmp(english[idx],"\0")==0) strcpy(english[idx],"-1");
    if (strcmp(program[idx],"\0")==0) strcpy(program[idx],"-1");
    idx++;
}
void print(char **names,char **maths,char **englishs,char **programs,int student) {
    int i;
    printf("name\tm\te\tp\n");
    for (i=0;i<student;i++) {
        if (strcmp(names[i],"\0")!=0) {
            if (strcmp(maths[i],"-1")==0 && strcmp(englishs[i],"-1")==0 && strcmp(programs[i],"-1")==0) {
                printf("%s\tx\tx\tx\n",names[i]);
            }
            if (strcmp(maths[i],"-1")==0 && strcmp(englishs[i],"-1")!=0 && strcmp(programs[i],"-1")!=0) {
                printf("%s\tx\t%s\t%s\n",names[i],englishs[i],programs[i]);
            }
            if (strcmp(maths[i],"-1")==0 && strcmp(englishs[i],"-1")==0 && strcmp(programs[i],"-1")!=0) {
                printf("%s\tx\tx\t%s\n",names[i],programs[i]);
            }
            if (strcmp(maths[i],"-1")==0 && strcmp(englishs[i],"-1")!=0 && strcmp(programs[i],"-1")==0) {
                printf("%s\tx\t%s\tx\n",names[i],englishs[i]);
            }
            if (strcmp(maths[i],"-1")!=0 && strcmp(englishs[i],"-1")==0 && strcmp(programs[i],"-1")!=0) {
                printf("%s\t%s\tx\t%s\n",names[i],maths[i],programs[i]);
            }
            if (strcmp(maths[i],"-1")!=0 && strcmp(englishs[i],"-1")==0 && strcmp(programs[i],"-1")==0) {
                printf("%s\t%s\tx\tx\n",names[i],maths[i]);
            }
            if (strcmp(maths[i],"-1")!=0 && strcmp(englishs[i],"-1")!=0 && strcmp(programs[i],"-1")==0) {
                printf("%s\t%s\t%s\tx\n",names[i],maths[i],englishs[i]);
            }
            if (strcmp(maths[i],"-1")!=0 && strcmp(englishs[i],"-1")!=0 && strcmp(programs[i],"-1")!=0) {
                printf("%s\t%s\t%s\t%s\n",names[i],maths[i],englishs[i],programs[i]);
            }
        }
    }
}
void sort(char **names,char **maths,char **englishs,char **programs,int student) {
    int i,j;
    char *temp = malloc(256*sizeof(char));
    char *temp2 = malloc(256*sizeof(char));
    char *temp3 = malloc(256*sizeof(char));
    char *temp4 = malloc(256*sizeof(char));
    for(i=0;i<student-1;i++){
		for(j=0;j<student-1-i;j++){
			if(strcmp(names[j],names[j+1])>0){
				temp=names[j];
				names[j]=names[j+1];
				names[j+1]=temp;
                temp2=maths[j];
				maths[j]=maths[j+1];
				maths[j+1]=temp2;
                temp3=englishs[j];
				englishs[j]=englishs[j+1];
				englishs[j+1]=temp3;
                temp4=programs[j];
				programs[j]=programs[j+1];
				programs[j+1]=temp4;
			}
		}
	}
}
void query(char **data,char **names,char **maths,char **englishs,char **programs,int student) {
    del(data[1],0,2);
    int i;
    for (i=0;i<student;i++) {
        if (strcmp(data[1],names[i])==0) {
            if (strcmp(maths[i],"-1")==0) {
                strcpy(maths[i],"x");
            }
            if (strcmp(englishs[i],"-1")==0) {
                strcpy(englishs[i],"x");
            }
            if (strcmp(programs[i],"-1")==0) {
                strcpy(programs[i],"x");
            }
            printf("%s\t%s\t%s\t%s\n",names[i],maths[i],englishs[i],programs[i]);
            break;
        }
    }
    if (i>=student) printf("Student %s not found.\n", data[1]);
}
void delete(char **data,char **names,int student) {
    del(data[1],0,2);
    int i;
    for (i=0;i<student;i++) {
        if (strcmp(data[1],names[i])==0) {
            strcpy(names[i],"\0");
            break;
        }
    }
    if (i>=student) printf("Student %s not found.\n", data[1]);
}
int main() {
    char *word = malloc(128*sizeof(char));
    char *line = malloc(128*sizeof(char));
    char *ptr;
    char ** data = malloc(128*sizeof(char*));
    char ** name = malloc(256*sizeof(char*));
    char **math = malloc(256*sizeof(char*));
    char **english = malloc(256*sizeof(char*));
    char **program = malloc(256*sizeof(char*));
    int cnt=0,i,studentnumber=0;
    int Ncnt=0,Mcnt=0,Pcnt=0,Ecnt=0;
    for (i = 0; i < 128; i++) {
        *(data+i)= malloc(36*sizeof(char));
    }
    for (i = 0; i < 256; i++) {
        *(name+i)= malloc(32*sizeof(char));
        *(math+i)= malloc(8*sizeof(char));
        *(english+i)= malloc(8*sizeof(char));
        *(program+i)= malloc(8*sizeof(char));
    }
    while (fgets(line,128,stdin)) {
        ptr = line;
        while (ptr=getword(ptr,word)) {
            if (word[0]=='p') {
                Pcnt++;
                if (Pcnt<=1) {
                    if (cnt==0) {
                        strcpy(data[0],word);
                        cnt++;
                    }
                    if (cnt>1) {
                        if (word[2]=='-') {
                            strcpy(data[0],"\0");
                            cnt++;
                        }
                        else if (isdigit(word[2]) || word[2]=='+') {
                            strcpy(data[cnt],word);
                            cnt++;
                        }
                        else if (!(isdigit(word[2])) && word[2]!='+'){
                            strcpy(data[0],"\0");
                            cnt++;
                        }
                    }
                }
                else if (Pcnt>1) {strcpy(data[0],"\0");cnt++;}
            }
            if (word[0]=='n') {
                Ncnt++;
                if (word[1]==':') {
                    if (Ncnt<=1) {
                        if(isalpha(word[2])) {
                            strcpy(data[cnt],word);
                            cnt++;
                        }
                        else {strcpy(data[0],"\0");cnt++;}
                    }
                    else if (Ncnt>1) {strcpy(data[0],"\0");cnt++;}
                }
                else if (word[1]!=':') {
                   strcpy(data[0],"\0");
                   cnt++;
                }
            }
            if (word[0]=='m' || word[0]=='e') {
                if (word[0]=='m') Mcnt++;
                if (word[0]=='e') Ecnt++;
                if (Ecnt<=1&&Mcnt<=1) {
                    if (word[2]=='-') {
                    strcpy(data[0],"\0");
                    cnt++;
                    }
                    else if (isdigit(word[2]) || word[2]=='+') {
                        strcpy(data[cnt],word);
                        cnt++;
                    }
                    else if (!(isdigit(word[2]) && word[2]!='+')){
                        strcpy(data[0],"\0");
                        cnt++;
                    }
                }
                else if (Ecnt>1 || Mcnt>1) {strcpy(data[0],"\0");cnt++;}
            }
            if (word[0]=='i'||word[0]=='s'||word[0]=='q'||word[0]=='d') {
                strcpy(data[cnt],word);
                cnt++;
            }
            if (word[0]!='i'&&word[0]!='s'&&word[0]!='q'&&word[0]!='d'&&word[0]!='n'&&word[0]!='p'&&word[0]!='m' && word[0]!='e') {
                strcpy(data[0],"\0");
                cnt++;
            }
        }
        Ncnt=0;
        Mcnt=0;
        Ecnt=0;
        Pcnt=0;
        if (cnt>5) {
            strcpy(data[0],"\0");
        }
        if (strcmp(data[0],"i")==0) {
            insert(data,cnt,name,math,english,program);
            studentnumber++;
        }
        else if (strcmp(data[0],"p")==0) {
            print(name,math,english,program,studentnumber);
        }
        else if (strcmp(data[0],"s")==0) {
            sort(name,math,english,program,studentnumber);
        }
        else if (strcmp(data[0],"q")==0) {
            query(data,name,math,english,program,studentnumber);
        }
        else if (strcmp(data[0],"d")==0) {
            delete(data,name,studentnumber);
        }
        else if (strcmp(data[0],"d")!=0&&strcmp(data[0],"q")!=0&&strcmp(data[0],"s")!=0&&strcmp(data[0],"p")!=0&&strcmp(data[0],"i")!=0) {
            printf("format error, please re-enter.\n");
        }
        cnt=0;
    }
    return 0;
}