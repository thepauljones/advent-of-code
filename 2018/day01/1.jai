
#import "Unicode";
#import "File_Utilities";
#import "String";
#import "Compiler";
#import "IntroSort";
#import "File";
#import "Program_Print";
#import "Hash_Table";
#import "Print_Color";
#import "Sort";

main :: () {
  file := read_entire_file("input.dat");
  bits := split(file, "\n");
  count := 0;

  for bits {
    print("Answer is %  \n", count);
    is_plus := starts_with(it, "+");

    value := string_to_int(slice(it, 1, it.count));

    if is_plus {
        count += value;
    } else {
        count -= value;
    }

    print("Answer is %  \n", count);
  }

  print("Ended: %\n", count);
}
