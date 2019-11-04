%global goipath         github.com/gogits/cron
%global commit          7f3990acf1833faa5ebd0e86f0a4c72a4b5eba3c
%global scm             git

%gometa

%global common_description %{expand:
A library ???
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                A library ???

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
