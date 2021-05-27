if exists('g:loaded_test')
  finish
endif
let g:loaded_test = 1

let s:save_cpo = &cpo
set cpo&vim

"{{{	CONTENTS
let g:test#test_GlobalVariable = "VARIABLE"
"}}}"
let &cpo = s:save_cpo
unlet s:save_cpo
