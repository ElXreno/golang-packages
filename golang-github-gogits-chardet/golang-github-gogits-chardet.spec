%global goipath         github.com/gogits/chardet
%global commit          2404f777256163ea3eadb273dada5dcb037993c0
%global scm             git

%gometa

%global common_description %{expand:
A library to automatically detect charset of texts for Go programming language.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                A library to automatically detect charset of texts for Go programming language.

License:                Custom
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
