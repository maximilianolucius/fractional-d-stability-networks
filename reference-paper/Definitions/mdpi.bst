%% Bibliography style for MDPI journals, updated on December 17, 2024

ENTRY
  { address
    archiveprefix %
    author
    booktitle
    chapter
    edition
    editor
    eprint %
    doi
    howpublished
    institution
    journal
    key
    month
    note
    number
    organization
    pages
    primaryclass %
    publisher
    school
    series
    title
    type
    volume
    year
    url
    urldate
    nationality
  }
  {}
  { label extra.label sort.label short.list }

INTEGERS { output.state before.all mid.sentence after.sentence after.block after.item }

FUNCTION {init.state.consts}
{ #0 'before.all :=
  #1 'mid.sentence :=
  #2 'after.sentence :=
  #3 'after.block :=
  #4 'after.item :=
}

STRINGS { s t }

FUNCTION {output.nonnull}
{ 's :=
  output.state mid.sentence =
    { ", " * write$ }
    { output.state after.block =
	{ add.period$ write$
	  newline$
	  "\newblock " write$
	}
	{ output.state before.all =
	    'write$
	    { output.state after.item =
	    {"; " * write$}
	    {add.period$ " " * write$} 
	    if$}
	  if$
	}
      if$
      mid.sentence 'output.state :=
    }
  if$
  s
}

FUNCTION {output}
{ duplicate$ empty$
    'pop$
    'output.nonnull
  if$
}

FUNCTION {output.check}
{ 't :=
  duplicate$ empty$
    { pop$ "empty " t * " in " * cite$ * warning$ }
    'output.nonnull
  if$
}

FUNCTION {output.checkwoa}
{ 't :=
  duplicate$ empty$
    { pop$ }
    'output.nonnull
  if$
}

FUNCTION {fin.entry}
{ add.period$
  write$
  newline$
}

FUNCTION {new.block}
{ output.state before.all =
    'skip$
    { after.block 'output.state := }
  if$
}

FUNCTION {new.sentence}
{ output.state after.block =
    'skip$
    { output.state before.all =
	'skip$
	{ after.sentence 'output.state := }
      if$
    }
  if$
}

FUNCTION {not}
{   { #0 }
    { #1 }
  if$
}

FUNCTION {and}
{   'skip$
    { pop$ #0 }
  if$
}

FUNCTION {or}
{   { pop$ #1 }
    'skip$
  if$
}

FUNCTION {new.block.checka}
{ empty$
    'skip$
    'new.block
  if$
}

FUNCTION {new.block.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.block
  if$
}

FUNCTION {new.sentence.checka}
{ empty$
    'skip$
    'new.sentence
  if$
}

FUNCTION {new.sentence.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.sentence
  if$
}

FUNCTION {field.or.null}
{ duplicate$ empty$
    { pop$ "" }
    'skip$
  if$
}

FUNCTION {emphasize}
{ duplicate$ empty$
    { pop$ "" }
    { "{\em " swap$ * "}" * }
  if$
}

FUNCTION {embolden}
{ duplicate$ empty$
    { pop$ "" }
    { "{\bf " swap$ * "}" * }
  if$
}

FUNCTION {website}
{ duplicate$ empty$
    { pop$ "" }
    { "\url{" swap$ * "}" * }
  if$
}

INTEGERS { nameptr namesleft numnames }

FUNCTION {format.names}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr "{vv~}{ll}{, jj}{, f{.}}." format.name$ 't :=
      nameptr #1 >
        {
          nameptr #10
          #1 + =
          numnames #10
          > and
            { "others" 't :=
              #1 'namesleft := }
            'skip$
          if$
          namesleft #1 >
            { "; " * t * }
            {
              s nameptr "{ll}" format.name$ duplicate$ "others" =
                { 't := }
                { pop$ }
              if$
              numnames #2 >
       { "" * }
		'skip$
	      if$
	      t "others" =
		{"; " * " et~al." * }
		{ "; " * t * }
	      if$
	    }
	  if$
	}
	't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {format.key}
{ empty$
    { key field.or.null }
    { "" }
  if$
}

FUNCTION {format.authors}
{ author empty$
    { "" }
    { author format.names }
  if$
}

FUNCTION {format.editors}
{ editor empty$
    { "" }
    { editor format.names
      editor num.names$ #1 >
	{ ", Eds." * }
	{ ", Ed." * }
      if$
    }
  if$
}




FUNCTION {format.title}
{ title empty$
    { "" }
    { title}
  if$
}

FUNCTION {format.number.patent}
{ number empty$
    { "" }
    { nationality empty$
    { number}
    { nationality " " * number *}
    if$
    }
  if$
}

FUNCTION {format.full.names}
{'s :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
      "{vv~}{ll}" format.name$ 't :=
      nameptr #1 >
        {
          namesleft #1 >
            { ", " * t * }
            {
              numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " et~al." * }
                { " and " * t * }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {author.editor.full}
{ author empty$
    { editor empty$
        { "" }
        { editor format.full.names }
      if$
    }
    { author format.full.names }
  if$
}



FUNCTION {author.full}
{ author empty$
    { "" }
    { author format.full.names }
  if$
}

FUNCTION {editor.full}
{ editor empty$
    { "" }
    { editor format.full.names }
  if$
}

FUNCTION {make.full.names}
{ type$ "book" =
  type$ "inbook" =
  or
    'author.editor.full
    { type$ "proceedings" =
        'editor.full
        'author.full
      if$
    }
  if$
}

FUNCTION {output.bibitem}
{ newline$
  "\bibitem[" write$
  label write$
  ")" make.full.names duplicate$ short.list =
     { pop$ }
     { * }
   if$
  "]{" * write$
  cite$ write$
  "}" write$
  newline$
  ""
  before.all 'output.state :=
}

FUNCTION {n.dashify}
{ 't :=
  ""
    { t empty$ not }
    { t #1 #1 substring$ "-" =
	{ t #1 #2 substring$ "--" = not
	    { "--" *
	      t #2 global.max$ substring$ 't :=
	    }
	    {   { t #1 #1 substring$ "-" = }
		{ "-" *
		  t #2 global.max$ substring$ 't :=
		}
	      while$
	    }
	  if$
	}
	{ t #1 #1 substring$ *
	  t #2 global.max$ substring$ 't :=
	}
      if$
    }
  while$
}


FUNCTION {format.date}
{ year empty$
    { month empty$
	{ "" }
	{ "there's a month but no year in " cite$ * warning$
	  month
	}
      if$
    }
    { " " year embolden * }
  if$
}

FUNCTION {format.bdate}
{ year empty$
    { month empty$
	{ "" }
	{ "there's a month but no year in " cite$ * warning$
	  month
	}
      if$
    }
    { " " year * }
  if$
}

FUNCTION {format.pdate}
{ year empty$
    { month empty$
	{ "" }
	{ "there's a month but no year in " cite$ * warning$
	  month
	}
      if$
    }
    {  month empty$
	{ " " year * }
	{ " " month * " " * year *  }
      if$}
  if$
}

FUNCTION {format.btitle}
{ title emphasize
}

FUNCTION {tie.or.space.connect}
{ duplicate$ text.length$ #3 <
    { "~" }
    { " " }
  if$
  swap$ * *
}

FUNCTION {either.or.check}
{ empty$
    'pop$
    { "can't use both " swap$ * " fields in " * cite$ * warning$ }
  if$
}

FUNCTION {format.bvolume}
{ volume empty$
    { "" }
    { "Vol." volume tie.or.space.connect
      series empty$
	'skip$
	{ ", " * series emphasize * }
      if$
      "volume and number" number either.or.check
    }
  if$
}

FUNCTION {format.number.series}
{ volume empty$
    { number empty$
	{ series field.or.null }
	{ output.state mid.sentence =
	    { "number" }
	    { "Number" }
	  if$
	  number tie.or.space.connect
	  series empty$
	    { "there's a number but no series in " cite$ * warning$ }
	    { " in " * series * }
	  if$
	}
      if$
    }
    { "" }
  if$
}

FUNCTION {format.edition}
{ edition empty$
    { "" }
    { output.state mid.sentence =
	{ edition "l" change.case$ " ed." * }
	{ edition "t" change.case$ " ed." * }
      if$
    }
  if$
}

INTEGERS { multiresult }

FUNCTION {multi.page.check}
{ 't :=
  #0 'multiresult :=
    { multiresult not
      t empty$ not
      and
    }
    { t #1 #1 substring$
      duplicate$ "-" =
      swap$ duplicate$ "," =
      swap$ "+" =
      or or
	{ #1 'multiresult := }
	{ t #2 global.max$ substring$ 't := }
      if$
    }
  while$
  multiresult
}

FUNCTION {format.pages}
{ pages empty$
    { "" }
    { pages multi.page.check
	{ "pp." pages n.dashify tie.or.space.connect }
	{ "p." pages tie.or.space.connect }
      if$
    }
  if$
}

FUNCTION {format.vol.num.pages}
{ volume emphasize field.or.null
  number empty$
    'skip$
    { 
      volume empty$
	{ "there's a number but no volume in " cite$ * warning$ }
	'skip$
      if$
    }
  if$
  pages empty$
    'skip$
    { duplicate$ empty$
	{ pop$ format.pages }
	{ ",~" * pages n.dashify * }
      if$
    }
  if$
}

FUNCTION {format.chapter.pages}
{ chapter empty$
    'format.pages
    { type empty$
	{ "chapter" }
	{ type "l" change.case$ }
      if$
      chapter tie.or.space.connect
      pages empty$
	'skip$
	{ ", " * format.pages * }
      if$
    }
  if$
}

FUNCTION {format.in.ed.booktitle}
{ booktitle empty$
    { "" }
    { editor empty$
	{ edition empty$
            {"In " booktitle emphasize *} 
            {"In " booktitle emphasize * ", " * edition * " ed." *}
          if$
         }
	{ edition empty$
            {"In " booktitle emphasize * "; " * format.editors * }
            {"In " booktitle emphasize * ", " * edition * " ed." * ";  " * format.editors * }
          if$
         }
      if$
    }
  if$
}

FUNCTION {format.in.ed.booktitle.proc}
{ booktitle empty$
    { "" }
    { editor empty$
	{ edition empty$
            {"In Proceedings of the " booktitle  *} 
            {"In Proceedings of the " booktitle  * ", " * edition * " ed." *}
          if$
         }
	{ edition empty$
            {"In Proceedings of the " booktitle  * "; " * format.editors * }
            {"In Proceedings of the " booktitle  * ", " * edition * " ed." * ";  " * format.editors * }
          if$
         }
      if$
    }
  if$
}

FUNCTION {format.publisher.and.address}
{ publisher empty$
    {""}
    { address empty$
       {publisher }
       {publisher ": " * address *}
    if$
    }
  if$
}



FUNCTION {empty.misc.check}
{ author empty$ title empty$ howpublished empty$
  month empty$ year empty$ note empty$
  and and and and and
    { "all relevant fields are empty in " cite$ * warning$ }
    'skip$
  if$
}

FUNCTION {format.thesis.type}
{ type empty$
    'skip$
    { pop$
      type "t" change.case$
    }
  if$
}

FUNCTION {format.tr.number}
{ type empty$
    { "Technical Report" }
    'type
  if$
  number empty$
    { "t" change.case$ }
    { number tie.or.space.connect }
  if$
}

FUNCTION {format.article.crossref}
{ key empty$
    { journal empty$
        { "need key or journal for " cite$ * " to crossref " * crossref *
          warning$
          ""
        }
        { "In \emph{" journal * "}" * }
      if$
    }
    { "In " }
  if$
  " \citet{" * crossref * "}" *
}



FUNCTION {format.book.crossref}
{ volume empty$
    { "empty volume in " cite$ * "'s crossref of " * crossref * warning$
      "In "
    }
    { "Vol." volume tie.or.space.connect
      " of " *
    }
  if$
  editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
	{ series empty$
	    { "need editor, key, or series for " cite$ * " to crossref " *
	      crossref * warning$
	      "" *
	    }
	    { "{\em " * series * "\/}" * }
	  if$
	}
	{ key * }
      if$
    }
    { "" * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {format.incoll.inproc.crossref}
{ editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
	{ booktitle empty$
	    { "need editor, key, or booktitle for " cite$ * " to crossref " *
	      crossref * warning$
	      ""
	    }
	    { "In {\em " booktitle * "\/}" * }
	  if$
	}
	{ "In " key * }
      if$
    }
    { "In " * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {format.website}
{ url empty$
    { "" }
    { "Available online: " url website *
     urldate empty$
    {"there is url but no urldate in " cite$ * warning$}
    { " (accessed on " * urldate * ")" *}
    if$
    }
  if$
}

%% the following function is modified from kp.bst at http://arxiv.org/hypertex/bibstyles/
FUNCTION {format.eprint}
{eprint empty$
	{ ""}
	{primaryClass empty$
		{" \href{http://arxiv.org/abs/" eprint * "}" *  "{{\normalfont " * "[" * eprint * "]" * "}}" *}
		{archivePrefix empty$
              		  {" \href{http://arxiv.org/abs/" eprint * "}" * "{{\normalfont " * "[" * "arXiv:" * primaryClass * "/" * eprint * "]" * "}}" *}
			  {" \href{http://arxiv.org/abs/" eprint * "}" * "{{\normalfont " * "[" * archivePrefix * ":" * primaryClass * "/" * eprint * "]" * "}}" *}
		if$
		}
	if$
	}
if$
}


%% For printing DOI numbers (it is a hyperlink but printed in black)
FUNCTION {formatfull.doi}
{ doi empty$
  { ""  }
  {"{\url{https://doi.org/" doi * "}}" * }
  if$
}



FUNCTION {article}
{ output.bibitem
  format.authors "author" output.check
  author format.key output
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { journal emphasize "journal" output.check
      format.date * format.vol.num.pages "" * output
    }
    { format.article.crossref output.nonnull
      format.pages output
    }
  if$
format.eprint output
new.block
note output
formatfull.doi output
fin.entry
}

FUNCTION {book}
{ output.bibitem
  author empty$
    { format.editors "author and editor" output.check }
    { format.authors output.nonnull
      crossref missing$
	{ "author and editor" editor either.or.check }
	'skip$
      if$
    }
  if$
  new.block
  format.btitle "title" output.check
  format.edition output
  after.item 'output.state :=
  crossref missing$
    { format.bvolume output
      format.number.series output
      format.publisher.and.address "publisher" output.check
%%%      address output
    }
    {
      format.book.crossref output.nonnull
    }
  if$
  format.bdate "year" output.check
  after.item 'output.state :=
  format.chapter.pages output
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {booklet}
{ output.bibitem
  format.authors output
  new.block
  format.title "title" output.check
  howpublished address new.block.checkb
  howpublished output
  address output
  format.bdate output
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {inbook}
{ output.bibitem
  author empty$
    { format.editors "author and editor" output.check }
    { format.authors output.nonnull
      crossref missing$
	{ "author and editor" editor either.or.check }
	'skip$
      if$
    }
  if$
%%%  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      after.item 'output.state :=
      format.number.series output
%%      new.sentence
      format.publisher.and.address "publisher" output.check
      format.bdate "year" output.check
      after.item 'output.state :=
      format.bvolume output
      format.chapter.pages "chapter and pages" output.check
      
    }
    { format.chapter.pages "chapter and pages" output.check
      new.block
      format.book.crossref output.nonnull
      format.bdate "year" output.check
    }
  if$
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {incollection}
{ output.bibitem
  format.authors "author" output.check
  new.block
  format.title "title" output.check
  new.sentence
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      after.item 'output.state :=
      format.number.series output
%      new.sentence
      format.publisher.and.address "publisher" output.check
      format.bdate "year" output.check
      after.item 'output.state :=
      format.bvolume output
      format.chapter.pages output
    }
    { format.incoll.inproc.crossref output.nonnull
      format.chapter.pages output
    }
  if$
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {inproceedings}
{ output.bibitem
  format.authors "author" output.check
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.in.ed.booktitle.proc "booktitle" output.check
      address empty$
	{ organization publisher new.sentence.checkb
	  organization output
	  publisher output
	  format.pdate "year" output.check
	}
	{ mid.sentence 'output.state :=
	  organization output
	  address output.nonnull
      format.pdate "year" output.check
      after.item 'output.state :=
	}
      if$
    format.number.series output
    format.bvolume output
    format.pages output
    }
    { format.incoll.inproc.crossref output.nonnull
      format.pages output
    }
  if$
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {conference} { inproceedings }

FUNCTION {manual}
{ output.bibitem
  author empty$
    { organization empty$
	'skip$
	{ organization output.nonnull
	  address output
	}
      if$
    }
    { format.authors output.nonnull }
  if$
  new.block
  format.btitle "title" output.check
  author empty$
    { organization empty$
	{ address new.block.checka
	  address output
	}
	'skip$
      if$
    }
    { organization address new.block.checkb
      organization output
      address output
    }
  if$
  format.edition output
  format.bdate output
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {mastersthesis}
{ output.bibitem
  format.authors "author" output.check
  new.block
  format.title "title" output.check
  new.block
  "Master's thesis" format.thesis.type output.nonnull
  school "school" output.check
  address output
  format.bdate "year" output.check
  format.eprint output
  new.block
  note output
  formatfull.doi output
  fin.entry
}

FUNCTION {misc}
{ output.bibitem
  format.authors output
  title howpublished new.block.checkb
  format.title output