#import "Basic";
#import "Hash_Table";
#import "String";
#import "File";

main :: () {
    file := read_entire_file("input.dat");
    lines := split(file, "\n");


    threes := 0;
    twos := 0;
    found_two := false;
    found_three := false;

    for lines {
        chars: Table(u8, u32, null, LOAD_FACTOR_PERCENT=70);

        for char: it {
          found, count := table_find_new(*chars, char);
          if found {
            table_set(*chars, char, count + 1);
          } else {
            table_add(*chars, char, 1);
          }
        }

        found_two = false;
        found_three = false;

        for chars {
            key, value := it_index, it;

            if value == 2 && !found_two {
                twos += 1;
                print("% ", value);
                print_character(key);
                print("\n");
                found_two = true;
            }

            if value == 3 && !found_three {
                threes += 1;
                print("3 ");
                print_character(key);
                found_three = true;
                print("\n");
            }
        }
    }

    print("Answer: % * % = %", twos, threes, twos * threes);

}
