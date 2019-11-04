%global goipath         github.com/ethantkoenig/rupture
%global commit          0a76f03a811abcca2e6357329b673e9bb8ef9643
%global scm             git

%gometa

%global common_description %{expand:
An explosive companion to the bleve indexing library
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                An explosive companion to the bleve indexing library

License:                MIT
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
