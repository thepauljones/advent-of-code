#import "Basic";
#import "String";
#import "File";

main :: () {
  required_digits:u8;
  required_digits = 12;

  file := read_entire_file("input.dat");
  lines := split(trim(file), "\n");

  answer := 0;

  for line:lines {
    l := string_to_chars(line);

    res : [..]u8;

    count := required_digits;
    while count > 0 {
      val, index, new_array := array_max(l, count);
      l = new_array;
      array_add(*res, val);
      count -= 1;
    }

    curr_answer := string_to_int(chars_to_string(res));
    answer += curr_answer;
  }

  print("%\n", answer);
}

array_max :: (a:[]u8, digits:u8, debug: bool = false) -> u8, int, []u8 {
    m :u8 = 0;
    index := 0;
    b := array_slice(a, a.count - digits);


    for b {
      if it > m {
        m = it;
        index = it_index;
      }
    }

    ret:[..]u8;

    for a {
      if it_index > index {
        array_add(*ret, it);
      }
    }

    return m, index, ret;
}

chars_to_string :: (chars: [] u8) -> string {
    s: string;
    s.count = chars.count;
    s.data = alloc(chars.count);
    for c, i: chars {
      s[i] = c;
    }

    return s;
}

string_to_chars :: (s: string) -> []u8 {
  l:[..]u8;
  for s {
    array_add(*l, it);
  }
  return l;
}

array_slice :: (a: []u8, length: int) -> []u8 {
  ret : [..]u8;
  for a {
    if it_index > length {
      return ret;
    }
    array_add(*ret, it);
  }
  return ret;
}
