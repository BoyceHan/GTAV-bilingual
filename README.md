﻿#- (english) Usage Guideline  -#
	This is an example guideline showing how to merge "american_rel.rpf" (US English) and "chinesesimp_rel.rpf" (Simplified Chinese)
	If you want to merge another two languages, you can do it with is .py script accordingly.

	1. Download GTAV
	
	2. DOwnload OpenIV
	
	3. Run OpenIV, select GTAV (Windows)
	
	4. Turn to ./update/update2.rpf/x64/data/lang
	
	5. In this directory you will find language packages such as "american_rel.rpf" and "chinesesimp_rel.rpf"
	
	6. Put this .py script in a directory (let us call it "./")
	
	7. Create a directory under "./" called "american", open "american_rel.rpf" and extract all .gxt2 files to "./american/"
	
	8. Create a directory under "./" called "chinesesimp", open "chinesesimp_rel.rpf" and extract all .gxt2 files to "./chinesesimp/"
	
	9. (1)  Make sure the Configs below (path_language1 and path_language2) are accordingly correct. One of them shold be "./chinesesimp/" and another should be "./american/"
	   
	   (2)  Whether which is language1 depends the order of languages you want when you play the game.
	        For example if you want to see
				"甩掉警察。Lose the cops." (chinese first, us-english second)
			then set path_language1='./chinesesimp/' path_language2='./american/'
			
	        and if you want to see
				"Lose the cops.甩掉警察。" (us-english first, chinese second)
			then set path_language1='./american/' path_language2='./chinesesimp/'
	   
	   (3) We recommand chinese first because almost all chinese subscripts are ending with chinese full-stop sign "。" with is a 2-width sign having a 1-width blank at the end.
	       This gives a clearer division between chinese and us-english subscripts[see example in 9(2)]. While english full-top sign "." cannot offer such beneift.
		   
	10. Create a directory under "./" called "merged". Make sure the Configs below (path_merged) are accordingly correct (should be "./merged/").
	
	11. Run this .py script. (of course you need to install python3 if you have not done so before)
	
	12. You will get new .gxt2 files in the directory "./merged/"

	13. Return to OpenIV, delete all .gxt2 files in "chinesesimp_rel.rpf" (we recommand you backup before deleteing, but they're already backed-up in "./chinesesimp", right? (laugh) )
	    and add all .gxt2 files in "./merged/" into "chinesesimp_rel.rpf"
	
		WARNING: you may want to delete all .gxt2 files in "american_rel.rpf" and add all .gxt2 files in "./merged/" into it.
		(so you have Chinese version and Chinese-English-bilingual version; anyway you do not play English-Solo version, right?)
		DO NOT DO SO.
		KEEP "american_rel.rpf" NOT MODIFIED ASSURES THAT YOU CAN ALWAYS RUN ENGLISH LANGUAGE VERSION OF GTAV CORRECTLY.
		English version is the most stable version of GTAV. Running of English version NEVER relys on other language packages. Vice NOT Versa, NOT. 
	
	14. In OpenIV install ASI Loader and OpenIV.ASI
	
	15. Run GTAV and enjoy!

Note: Should you fail to find the files mentioned by section 5 of this tutorial in the directory mentioned by section 4, try a global search of the filename "abgail2.gxt2" and look for the rpf file which contains this gxt2 file, and in the name of which there is "chinesesimp". Under the same directory, find the rpf file in the name of which there is "american". Then conduct the remaining operation in reference of this tutorial.

#- (chinese) 使用教程  -#
	此为示例教程，说明如何把 "american_rel.rpf" （美式英语）和 "chinesesimp_rel.rpf" （简体中文合并）
	如果您想要合并其他两种语言，请比照此教程使用本.py脚本

	1. 下载GTAV
	
	2. 下载OpenIV
	
	3. 启动OpenIV, 选择GTAV (Windows)
	
	4. 进入目录 ./update/update2.rpf/x64/data/lang
	
	5. 在此目录中您将找到若干语言包，其名称类似于 "american_rel.rpf" 和 "chinesesimp_rel.rpf"
	
	6. 把此.py脚本放在一个独立的目录中（下文把这个目录位置称为"./"）
	
	7. 在 "./" 下创建一个名为 "american" 的新目录, 打开 "american_rel.rpf" 并提取所有 .gxt2 文件至 "./american/" 目录
	
	8. 在 "./" 下创建一个名为 "chinesesimp" 的新目录, 打开 "chinesesimp_rel.rpf" 并提取所有 .gxt2 文件至 "./chinesesimp/" 目录
	
	9. (1)  确保下方的配置参数 (path_language1 and path_language2) 正确，与上述目录名一致。 其中一个参数须设置为 "./chinesesimp/", 另一个须为 "./american/"
	   
	   (2)  至于哪个须设置为language1取决于您想在游戏中见到怎样的语言顺序。
	        例如，如果您想见到
				"甩掉警察。Lose the cops." (中文在前，英文在后)
			就设置 path_language1='./chinesesimp/' path_language2='./american/'
			
	        如果您想见到
				"Lose the cops.甩掉警察。" (英文在前，中文在后)
			就设置 path_language1='./american/' path_language2='./chinesesimp/'
	   
	   (3) 推荐设置中文在前，因为大多数中文字幕都以中文句号 "。" 结尾，这个字符是2宽度的，末尾有1宽度空白。
	       这使得中文和英文字幕的界限很清晰[参见9(2)中的例子]. 英语句号 "." 就没有这个好处了。
		   
	10.  在 "./" 下创建一个名为 "merged" 的新目录。 确保下方的配置参数 (path_merged) 正确，与上述目录名一致。 (应为 "./merged/").
	
	11. 运行此 .py 脚本. （当然你得安装python3才能运行，如果你之前没装过的话）
	
	12. 您会在 "./merged/" 目录中得到若干 .gxt2 文件

	13. 回到OpenIV, 删除 "chinesesimp_rel.rpf" 中的所有 .gxt2文件 （我们建议您删除前先备份，但刚刚已经备份到"./chinesesimp/"里了不是吗？（笑））
		并将 "./merged/" 目录中所有 .gxt2 文件 导入 "chinesesimp_rel.rpf"
	
		警告: 您可能想删除"./american_rel.rpf"文件中所有.gxt2文件并把"./merged/"中的所有.gxt2文件导入进去
		（这样就有中文、中英两个版本玩了！反正我也不玩纯英文版。）
		不要这样做，绝对不要。
		保持 "american_rel.rpf" 不变，这能保证英语版本永远是正确无误的。英语版本是GTAV最稳定的版本，运行英语版不依赖其他语言包。反之不然，不然！
	
	14. 在OpenIV中安装ASI Loader和OpenIV.ASI
	
	15. 打开GTAV，开玩。

注：如果你发现在本教程第4条指定的路径下没有第5条所说的文件，可能是由于版本更新造成语言包位置发生变化。请在OpenIV中对“abgail2.gxt2”这个文件进行全局搜索，找到名称中含有chinesesimp并含有这个gxt2文件的rpf包。在同一目录下找到名称中含有american的rpf包。参照本教程的剩余步骤操作。
 
![image](https://github.com/GodCallMeGod/GTAV-bilingual/blob/main/pics/1.jpg)
![image](https://github.com/GodCallMeGod/GTAV-bilingual/blob/main/pics/2.jpg)
![image](https://github.com/GodCallMeGod/GTAV-bilingual/blob/main/pics/3.jpg)
![image](https://github.com/GodCallMeGod/GTAV-bilingual/blob/main/pics/4.jpg)
![image](https://github.com/GodCallMeGod/GTAV-bilingual/blob/main/pics/5.jpg)
