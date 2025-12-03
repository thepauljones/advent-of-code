#import "Basic";
#import "String";
#import "File";

main :: () {
  file := read_entire_file("input.dat");
  lines := split(trim(file), "\n");

  answer := 0;

  for line:lines {
    l:[..]u8;
    for line {
      array_add(*l, it);
    }
    first, f_index := array_max(l);
    
    if f_index == l.count - 1 {
      first, f_index = array_max(l, first);
    }

    l2: [..]u8;
    for l {
      if it_index <= f_index continue;
      array_add(*l2, it);
    }
    second, s_index := array_max(l2);

    builder: String_Builder;
    append(*builder, first);
    append(*builder, second);

    val := builder_to_string(*builder);
    answer += string_to_int(val);
  }

  print("%\n", answer);
}

array_max :: (a:[]u8, under: u8 = 58) -> u8, int {
    m :u8 = 0;
    index := 0;
    for a {
      if it > m && it < under {
        m = it;
        index = it_index;
      }
    }

    return m, index;
}
