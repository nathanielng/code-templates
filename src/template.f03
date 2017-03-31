subroutine my_sub(input_file)
    implicit none
    character(len=*), intent(in) :: input_file
    logical :: is_file

    inquire(file=input_file, exist=is_file)
    if (is_file.EQV..TRUE.) then
        write(*,'(A)') "Input file: '"//trim(input_file)//"'"
    else
        write(*,'(A)') "Input file: '"//trim(input_file)//"' (file does not exist)"
    endif
end subroutine my_sub

program main
    implicit none
    character(len=255) :: str
    integer :: argc

    argc=command_argument_count()
    if (argc.LE.0) then
        call get_command_argument(0, str) 
        write(*,'(A)') "Usage: "//trim(str)//" [input_file]"
    else
        call get_command_argument(1, str)
        call my_sub(str)
    endif
end program main
