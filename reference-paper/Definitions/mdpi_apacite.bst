%% This is file `mdpi_apacite.bst',
%% Modified by MDPI according to apacite.bst. (Updated on 12 January 2025)
%%
%% The original source files were:
%%
%% apacite.dtx  (with options: `bibstyle')
%% 
%% This is a generated file.
%% 
%% Copyright (C) 1994-2013 Erik Meijer and any individual authors listed
%% elsewhere in this file.

ENTRY
  { address
    annote
    annotate
    author
    booktitle
    chair
    chapter
    day
    doi
    edition
    editor
    englishtitle
    firstkey
    howpublished
    institution
    journal
    key
    lastchecked
    month
    nihms
    note
    number
    organization
    originaladdress
    originalbooktitle
    originaledition
    originaleditor
    originaljournal
    originalnumber
    originalpages
    originalpublisher
    originalvolume
    originalyear
    pages
    pmcid
    publisher
    school
    series
    symposium
    text
    title
    translator
    type
    url
    urldate
    volume
    year
  }
  { cite.order             %% order of first citation
    title.number           %% for sorting titles
    cite.initials          %% dummy (0-1) indicating whether or not
                           %% initials of the 1st author must
                           %% be used for citing
    cite.num.names.full    %% number of names to be cited for full and
    cite.num.names.short   %% short cite
    add.to.year            %% For a, b, c, etc. after year
                           %% in multiple citations with same author-year
  }
  { year.label             %% For sorting entries by year
    author.year.sort.label %% For sorting entries and checking whether
                           %% initials should be added, how many authors
                           %% should be cited and whether a, b, etc.
                           %% after year is necessary
    title.sort.label       %% for sorting titles
    citeorder.sort.label   %% for sorting by citation order
    type.2                 %% Replacement for type with misc entries and
                           %% entries that revert to misc.
  }
INTEGERS { len  pos  name.max  old.number  numnames  numnames.old
           nameptr  lastname  format.num.names  cite.initials.old
           cite.num.names.old add.to.year.old  forward
           multiresult  dot brace.level
         }

STRINGS  { s  t  u old.label  field
           aut1f  aut1s  aut1f.old  aut1s.old
           aut2          aut2.old
           aut3          aut3.old
           aut4          aut4.old
           aut5          aut5.old
           aut6          aut6.old
           year.label.old
         }
FUNCTION {test} { #0 }
FUNCTION {dump.stack}
{ "---- STACK {" cite$ * "} ----" * top$
  stack$
  "---- END STACK {" cite$ * "} ----" * top$
}
FUNCTION {make.index} { #0 }
FUNCTION {unsorted} { #0 }
MACRO {jan}    {"{\APACmonth{01}}"}
MACRO {feb}    {"{\APACmonth{02}}"}
MACRO {mar}    {"{\APACmonth{03}}"}
MACRO {apr}    {"{\APACmonth{04}}"}
MACRO {may}    {"{\APACmonth{05}}"}
MACRO {jun}    {"{\APACmonth{06}}"}
MACRO {jul}    {"{\APACmonth{07}}"}
MACRO {aug}    {"{\APACmonth{08}}"}
MACRO {sep}    {"{\APACmonth{09}}"}
MACRO {oct}    {"{\APACmonth{10}}"}
MACRO {nov}    {"{\APACmonth{11}}"}
MACRO {dec}    {"{\APACmonth{12}}"}
MACRO {winter} {"{\APACmonth{13}}"}
MACRO {spring} {"{\APACmonth{14}}"}
MACRO {summer} {"{\APACmonth{15}}"}
MACRO {fall}   {"{\APACmonth{16}}"}
FUNCTION {not}
{   { #0 }
    { #1 }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {and}
{   'skip$
    { pop$ #0 }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {or}
{   { pop$ #1 }
    'skip$
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % issues warning if field is empty
    % call with
    %    "field"  field  warning.if.empty
    % Note that the first field must be between quotes
    % because it is the fieldname for use in the warning message.
    %
FUNCTION {warning.if.empty}
{ empty$
    { "No "  swap$ * " in " * cite$ * warning$ }
    { pop$ }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % issues warning if title, type, and howpublished are empty
    %
FUNCTION {check.relevant.fields}
{ title        empty$
  type         empty$ and
  howpublished empty$ and
    { "No title, type, and howpublished in " cite$ * warning$ }
    'skip$
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % delivers 1 if (both editor and translator
    %                not empty and not equal to each other)
    %          0 if (editor or translator empty) or
    %               (editor = translator)
    %
FUNCTION {editor.ne.trans}
{ translator empty$
    { #0 }
    { editor empty$
        { #0 }
        { translator editor =
            { #0 }
            { #1 }
          if$
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {conv.int.to.str}
{ duplicate$ #10 <
    { "0000" swap$ int.to.str$ * }
    { duplicate$ #100 <
        { "000" swap$ int.to.str$ * }
        { duplicate$ #1000 <
            { "00" swap$ int.to.str$ * }
            { duplicate$ #10000 <
                { "0" swap$ int.to.str$ * }
                { int.to.str$ }
              if$
            }
          if$
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {ref.type}
{ type$ "article"      =
    type$ "magazine"     =
      type$ "newspaper"    =
        type$ "book"         =
          type$ "techreport"   =
            type$ "unpublished"  =
              type$ "misc"         =
                type$ "booklet"      =
                  type$ "manual"       =
                    type$ "proceedings"  =
                    or
                  or
                or
              or
            or
          or
        or
      or
    or
    { #1 }
    { type$ "incollection"   =
        type$ "phdthesis"      =
          type$ "mastersthesis"  =
            type$ "lecture"        =
              type$ "inbook"         =
                type$ "inproceedings"  =
                  type$ "conference"  =
                    type$ "intechreport"   =
                    or
                  or
                or
              or
            or
          or
        or
        { #2 }
        { type$ "literal" =
            { #3 }
            { #0 }
          if$
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {is.atype}
{ type$ "article"        =
    type$ "magazine"       =
      type$ "newspaper"      =
        type$ "incollection"   =
          type$ "inbook"         =
            type$ "inproceedings"  =
              type$ "conference"  =
                type$ "intechreport"   =
                  type$ "manual"         =
                  or
                or
              or
            or
          or
        or
      or
    or
    { #1 }
    { journal empty$ not
        %
      type$ "phdthesis"      =
        type$ "mastersthesis"  =
        or
        %
      and
        { #1 }
        { type$ "misc" =
          type empty$ not and
            { type "\bibmessage" =
                type "\bibcomputerprogram" =
                  type "\bibcomputerprogrammanual" =
                    type "\bibcomputerprogramandmanual" =
                      type "\bibcomputersoftware" =
                        type "\bibcomputersoftwaremanual" =
                          type "\bibcomputersoftwareandmanual" =
                            type "\bibprogramminglanguage" =
                            or
                          or
                        or
                      or
                    or
                  or
                or
                { #1 }
                { #0 }
              if$
            }
            { #0 }
          if$
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % connects two strings with connect string
    % if one of them empty, then connect string
    % is left out
    %
    % call with S1 S2 connectstring connect.check
    %
FUNCTION {connect.check}
{ 'u :=
    %
    % if S2 = ""
    %
  duplicate$ empty$
      %
      % then remove S2
      %
    { pop$
        %
        % S1 is on top of stack.
        % if it is empty, it is replaced by the empty string ""
        %
      duplicate$ empty$
        { pop$ "" }
        'skip$
      if$
    }
      %
      % else swap S1 and S2 so that S1 can be checked
      %
    { swap$
        %
        % if S1 is empty, remove S1 so that S2 is left on the
        % stack and is the result is given
        %
      duplicate$ empty$
        { pop$ }
            %
            % now the real work starts:
            % push the connect string "C"
            % so that top of stack is "C" "S1" "S2"
            % concatenate, so that top of stack is
            % "S1+C" "S2"
            %
        { u *
            %
            % swap and concatenate
            %
          swap$ *
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % connects two strings with space ("\ ")
    % if length of second is 4 or larger,
    % connects them with non-breaking space ("tie", "~")
    % if length of second smaller than 4
    %
    % call with S1 S2 tie.or.space.connect
    % result: "S1\ S2" or "S1~S2"
    %
FUNCTION {tie.or.space.connect}
{ duplicate$ text.length$ #4 <
    { "~" }
    { "\ " }
  if$
  swap$ * *
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % connects two strings with comma (", ")
    % if one of them is empty, the comma is left out
    %
    % call with S1 S2 connect.with.comma.check
    % result: "S1, S2"
    %
FUNCTION {connect.with.comma.check}
{ ", " connect.check }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % connects two strings with semicolon ("; ")
    % if one of them is empty, semicolon is left out
    %
    % call with S1 S2 connect.with.semicolon.check
    % result: "S1; S2"
    %
FUNCTION {connect.with.semicolon.check}
{ "; " connect.check }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % connects two strings with colon (": ")
    % if one of them is empty, colon is left out
    %
    % call with S1 S2 connect.with.colon.check
    % result: "S1: S2"
    %
FUNCTION {connect.with.colon.check}
{ ": " connect.check }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % connects two strings with space ("\ ")
    %
    % call with S1 S2 connect.with.space.check
    % result: "S1\ S2"
    %
FUNCTION {connect.with.space.check}
{ "\ " connect.check }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % encloses string in pre- and postfix string
    % call with
    %    prefix postfix  S  enclose.check
    % delivers empty string if S empty
    %
FUNCTION {enclose.check}
{ duplicate$ empty$
    { pop$ pop$ pop$
      ""
    }
    { swap$ * * }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % emphasizes top of stack
    % call with
    %     "string" emphasize.check
    %
FUNCTION {emphasize.check}
{ "\Bem{" swap$
  "}"     swap$
  enclose.check
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % brackets top of stack
    % call with
    %     "string" bracket
    %
FUNCTION {bracket.check}
{ "[" swap$
  "]" swap$
  enclose.check
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % parenthesizes top of stack
    % call with
    %     "string" parenthesize
    %
FUNCTION {parenthesize.check}
{ "(" swap$
  ")" swap$
  enclose.check
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % checks whether argument is "multiresult":
    % whether it contains '-', '+', or ',' characters
    % used with pages to check whether pp. or p. must be used
    %
FUNCTION {multi.result.check}
{ 't :=
  #0 'multiresult :=
  %
  % while (not multiresult) and (length(t) > 1) do
  %
    { multiresult not
      t text.length$ #1 >
      and
    }
        %
        % if t(1-2) = "--" or t(1) = "+" or ","
        % then  multiresult = 1
        % else  t = t(2-last)
        %
    { t #1 #2 substring$ 's :=
      "--" s =
        { #1 'multiresult := }
        { t #1 #1 substring$ 's :=
          "+" s =
            "," s =
            or
            { #1 'multiresult := }
            { t #2 global.max$ substring$ 't := }
          if$
        }
      if$
    }
  while$
  multiresult
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % Checks whether an author is a corporate author, i.e.,
    % whether the field starts with "{\bibcorporate".
    % Call with
    %   field is.bibcorporate
    %
FUNCTION {is.bibcorporate}
{ #1 #14 substring$ "{\bibcorporate" = }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {sortify}
{ purify$
  "l" change.case$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {remove.spaces}
{   % Remove spaces from string.
    % Works best if string only contains alphanumeric characters and spaces.
  's :=                    % The original string
  s text.length$ 'len :=   % Its length (no. of characters)
  "" 't :=                 % Initialize the transformed string
  #0 'pos :=
    %
    % while (pos < len) do
    %
  { pos len < }
    { pos #1 +  'pos :=
      s pos #1 substring$  'u :=
        %
        % u is the pos-th character in s
        % If it is a space, move to next character,
        % else copy character to output.
        %
      u " " =
        'skip$
        { t u *  't := }
      if$
    }
  while$
    %
    % Now push the result back on the stack
  t
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % end block by writing what's left on the stack and
    % starting a new line
    %
FUNCTION {output.end.block}
{ write$
  newline$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % end block by adding a period and writing what's left
    % on the stack and starting a new line
    %
FUNCTION {output.dot.end.block}
{ add.period$
  output.end.block
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % starting new block by writing what's left on the stack,
    % starting a new line and adding some extra space or
    % whatever is more defined in \newblock
    %
FUNCTION {output.new.block}
{ output.end.block
  "\newblock " write$ 
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % starting new block by writing what's left on the stack,
    % starting a new line and adding some extra space or
    % whatever is more defined in \newblock
    %
FUNCTION {output.dot.new.block}
{ add.period$
  output.new.block
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {start.new.block}
{ " " write$ newline$
  "\newblock " write$ newline$
}

FUNCTION {sort.name.format.classic} { "{ll{}}{  f{}}{  vv{}}{  jj{}}" }

FUNCTION {cite.name.format.classic} { "{ll}" }

FUNCTION {author.name.format.classic} { "{ll}{, f{.  }.}{ vv}{, jj}" }

FUNCTION {index.name.format.classic} { "{ll}{, f{.  }.}{ vv}{, jj}" }

FUNCTION {sort.name.format} { "{vv{}}{ll{}}{  f{}}{  jj{}}" }

FUNCTION {cite.name.format} { "{vv }{ll}" }

FUNCTION {cite.initials.name.format} { "{f{.  }.~~}{vv }{ll}{ jj}" }

FUNCTION {author.name.format} { "{vv }{ll}{, f{.  }.}{, jj}" }

FUNCTION {editor.name.format} { "{f{.  }.~~}{vv }{ll}{ jj}" }

FUNCTION {index.name.format} { "{vv }{ll}{, f{.  }.}{, jj}" }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {init.initials}
{ "yyyyy"  'aut1f.old :=
  "yyyyy"  'aut1s.old :=
  #0       'cite.initials.old :=
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {update.no.initials}
{ 'field :=
  field  'aut1f.old :=
  field  'aut1s.old :=
  #0     'cite.initials.old :=
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {check.add.initials.aut}
{   %
    % If last name is equal to previous last name
    % but initials are different, then initials should
    % be cited. If initials are also the same, initials
    % should be cited if that is the case for the previous
    % author .
    %
  aut1s aut1s.old =
    { aut1f aut1f.old =
        { cite.initials.old  'cite.initials := }
        { #1             'cite.initials :=
          aut1f          'aut1f.old :=
          aut1s          'aut1s.old :=
          cite.initials  'cite.initials.old :=
        }
      if$
    }
    {  %
       % Different last name.
      aut1f          'aut1f.old :=
      aut1s          'aut1s.old :=
      cite.initials  'cite.initials.old :=
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {check.add.initials.field}
{ 'field :=
  field #1 cite.initials.name.format format.name$  'aut1f :=
  field #1 cite.name.format          format.name$  'aut1s :=
    %
    % Now do the actual work
    %
  check.add.initials.aut
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {check.add.initials}
{   %
    % Check whether author or editor or other field acts as author.
    % Initials are only relevant with author or editor.
    %
  firstkey empty$ not
    { key empty$ not
        {   %
            % Both key and firstkey are nonempty.
            % Then, key is treated as last name of first author,
            % and firstkey is treated as last name + initials of
            % first author .
            %
          firstkey  sortify  remove.spaces  'aut1f :=
          key       sortify  remove.spaces  'aut1s :=
          check.add.initials.aut
        }
        { firstkey  sortify  remove.spaces  update.no.initials }
      if$
    }
    { key empty$ not
        { key  sortify  remove.spaces  update.no.initials }
        {   %
            % No key or firstkey, so find out which field
            % to use as author.
            %
            % Check reference type:
            %   if result is 1 then possibly editor acts as author
            %                2 then editor does not act as author
            %                3 then key should have been used
            %                0 then unknown reference type
          ref.type  #2 =
            {   %
                % Format first author with and without initials
              author empty$
                { title.sort.label  update.no.initials }
                { author  check.add.initials.field }
              if$
            }
            {   %
                % Format first author with and without initials
              author empty$
                { editor empty$
                    { title.sort.label  update.no.initials }
                    { editor check.add.initials.field }
                  if$
                }
                { author check.add.initials.field }
              if$
            }
          if$
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {tentative.cite.num.names.field} %% MDPI Modified
{ 'field :=
  field num.names$  'numnames :=
  numnames #3 <
    {   %
        % 1 or 2 names: always cite all of them.
      numnames  'cite.num.names.full  :=
      numnames  'cite.num.names.short :=
    }
    { numnames #6 <
        {   %
            % 3-5 names: cite all of them the first time,
            % only the first name later times
          numnames  'cite.num.names.full  :=
          #1        'cite.num.names.short :=
        }
        {   %
            % 6 or more names: cite only the first name
          #1  'cite.num.names.full  :=
          #1  'cite.num.names.short :=
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {tentative.cite.num.names}
{   %
    % Check whether author or editor or other field acts as author.
    % Number of names is only relevant with author or editor.
    %
  firstkey empty$ not
    {
      #1 'cite.num.names.full  :=
      #1 'cite.num.names.short :=
    }
    { key empty$ not
        {
          #1 'cite.num.names.full  :=
          #1 'cite.num.names.short :=
        }
        {   %
            % No key or firstkey, so find out which field
            % to use as author.
            %
            % Check reference type:
            %   if result is 1 then possibly editor acts as author
            %                2 then editor does not act as author
            %                3 then key should have been used
            %                0 then unknown reference type
          ref.type  #2 =
            {   %
                % Format first author with and without initials
              author empty$
                {
                  #1 'cite.num.names.full  :=
                  #1 'cite.num.names.short :=
                }
                { author tentative.cite.num.names.field }
              if$
            }
            {   %
                % Format first author with and without initials
              author empty$
                { editor empty$
                    {
                      #1 'cite.num.names.full  :=
                      #1 'cite.num.names.short :=
                    }
                    { editor tentative.cite.num.names.field }
                  if$
                }
                { author tentative.cite.num.names.field }
              if$
            }
          if$
        }
      if$
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {init.cite.num.names}
{ #0      'cite.num.names.old  :=
  #0      'numnames.old        :=
  "yyyy"  'year.label.old      :=
  #0      'add.to.year.old     :=
  ""      'aut1f.old           :=
  ""      'aut2.old            :=
  ""      'aut3.old            :=
  ""      'aut4.old            :=
  ""      'aut5.old            :=
  ""      'aut6.old            :=
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {update.cite.num.names}
{ cite.num.names.short  'cite.num.names.old  :=
  numnames              'numnames.old        :=
  year.label            'year.label.old      :=
  add.to.year           'add.to.year.old     :=
  aut1f                 'aut1f.old           :=
  aut2                  'aut2.old            :=
  aut3                  'aut3.old            :=
  aut4                  'aut4.old            :=
  aut5                  'aut5.old            :=
  aut6                  'aut6.old            :=
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {format.6.authors}
{   %
    % First author: with initials.
    %
  field #1 cite.initials.name.format format.name$  'aut1f :=
    %
    % Second and later authors: without initials.
    %
  numnames #1 >
    name.max #1 >
      and
    {   %
        % 2nd author
      field #2 cite.name.format format.name$  'aut2 :=
        %
      numnames #2 >
        name.max #2 >
          and
        {   %
            % 3nd author
          field #3 cite.name.format format.name$  'aut3 :=
            %
          numnames #3 >
            name.max #3 >
              and
            {   %
                % 4th author
              field #4 cite.name.format format.name$  'aut4 :=
                %
              numnames #4 >
                name.max #4 >
                  and
                {   %
                    % 5th author
                  field #5 cite.name.format format.name$  'aut5 :=
                    %
                  numnames #5 >
                    name.max #5 >
                      and
                    {   %
                        % 6th author
                      field #6 cite.name.format format.name$  'aut6 :=
                    }
                    {   %
                        % 5 authors: 6 is empty
                        %
                      "" 'aut6 :=
                    }
                  if$
                }
                {   %
                    % 4 authors: 5-6 are empty
                    %
                  "" 'aut5 :=
                  "" 'aut6 :=
                }
              if$
            }
            {   %
                % 3 authors: 4-6 are empty
                %
              "" 'aut4 :=
              "" 'aut5 :=
              "" 'aut6 :=
            }
          if$
        }
        {   %
            % 2 authors: 3-6 are empty
            %
          "" 'aut3 :=
          "" 'aut4 :=
          "" 'aut5 :=
          "" 'aut6 :=
        }
      if$
    }
    {   %
        % Only 1 author: 2-6 are empty
        %
      "" 'aut2 :=
      "" 'aut3 :=
      "" 'aut4 :=
      "" 'aut5 :=
      "" 'aut6 :=
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

FUNCTION {change.add.to.year}
{
  forward  #1  =
    {   %
        % Moving forward: this add.to.year number must be 1 higher than
        % previous.
        %
      add.to.year.old  #0  >
        { add.to.year.old  #1 +    'add.to.year  := }
        { #2  'add.to.year  := }
      if$
    }
    {   %
        % Moving backward: this add.to.year number must be 1 lower than
        % previous.
        %
      add.to.year.old  #1 -    'add.to.year  :=
    }
  if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
