#include <stdio.h>
#include <stdlib.h>
#include "ArrayList.h"
#include "Point.h"

int main(void){

    List list;
    Point compPos;
    Point* ppos;

    ListInit(&list);

    //4개의 데이터 저장//
    //1
    ppos = (Point*)malloc(sizeof(Point));
    SetPointPos(ppos, 2, 1);
    LInsert(&list, ppos);

    //2
    ppos = (Point*)malloc(sizeof(Point));
    SetPointPos(ppos, 2, 2);
    LInsert(&list, ppos);

    //3
    ppos = (Point*)malloc(sizeof(Point));
    SetPointPos(ppos, 3, 1);
    LInsert(&list, ppos);

    //4
    ppos = (Point*)malloc(sizeof(Point));
    SetPointPos(ppos, 3, 2);
    LInsert(&list, ppos);


    //저장된 데이터의 출력//
    printf("현재 데이터의 수 : %d \n", LCount(&list));

    if(LFirst(&list, &ppos)){
        ShowPointPos(ppos);  //출력해서 보여줌

        while(LNext(&list, &ppos)){
            ShowPointPos(ppos);
        }
    }

    printf("============ \n");

    //xpos가 2인 모든 데이터 삭제//
    compPos.xpos=2;
    compPos.ypos=0;

    if(LFirst(&list, &ppos)){

        if(PointComp(ppos, &compPos) == 1){
            //ppos=LRemove(&list);  //ppos는 Point형이다.
            LRemove(&list);  //삭제

            free(ppos);
        }

        while(LNext(&list,&ppos)){

            if(PointComp(ppos, &compPos) == 1){
                //ppos=LRemove(&list);
                LRemove(&list); //삭제

                free(ppos);
            }
        }


    }

    //삭제 후 남은 데이터 전체 출력//
    printf("현재 데이터 수 : %d \n", LCount(&list));

    if(LFirst(&list, &ppos)){
        ShowPointPos(ppos);  //출력해서 보여줌

        while(LNext(&list, &ppos)){
            ShowPointPos(ppos);
        }
    }




    return 0;
}