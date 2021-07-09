#define SEQ_LEN 61
#define NAME_LEN 16
#define LEN 77
//Константы, обозначающие длины последовательности в каждой строке файла выравнивания


#include "stdio.h"
#include "string.h"
#include "stdlib.h"
//Все нужные библиотеки - тут

char* get_sequence(char line[LEN]){
	char *sequence = malloc (sizeof (char) * SEQ_LEN);
	for(int i = 0; i < 61; i++){
		sequence[i] = line[i+16];
	}
	return sequence;
}
//Функция, которая вычленяет саму последовательность из строки файла
 
int main(){

	FILE *aln, *res;

	char aln_name[] = "cons_test.aln"; //ТУТ название файла с выравниванием
	char res_name[] = "con_res.aln";

	if ((aln = fopen(aln_name, "r")) == NULL){
		printf("Ошибка. Не удалось открыть файл.");
		return 0;
	}
//В случае чего он может выдать ошибку

	res = fopen(res_name, "w");
	
	char sequence_str[LEN];
	while (fgets(sequence_str, LEN ,aln) != NULL){
		char* seq_only = get_sequence(sequence_str);
	
		if(strcmp(seq_only,"------------------------------------------------------------") != 0){
			fputs(sequence_str, res);
		}
	
	}
		fclose(aln);
		fclose(res);
		
		return 0;	
}



