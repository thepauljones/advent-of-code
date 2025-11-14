#import "Basic";
#import "Hash_Table";
#import "String";
#import "File";

get_common_letters_and_count :: (one:string, two:string) -> string, u8 {
  common:string;
  count :u8;

  builder: String_Builder;
  init_string_builder(*builder);

  for one {
      if it == two[it_index] {
        append(*builder, it);
      } else {
        count += 1;
      }
  }

  common = builder_to_string(*builder);
  return common, count;
}

main :: () {
    file := read_entire_file("input.dat");
    lines := split(file, "\n");

    for lines { 
      for wank:lines {
          if it == wank || it.count == 0 || wank.count == 0 {
              continue;
          }

          res, count := get_common_letters_and_count(it, wank);
          if count == 1 {
              print("Answer: %\n", res);
              exit(0);
          }

        }
    }
}
